from rest_framework import serializers

from .models import SecureFile
from django.contrib.auth import get_user_model

User = get_user_model()

class SecureFileSerializers(serializers.ModelSerializer):

    shared_with = serializers.SlugRelatedField(
        many = True,
        slug_field= 'username',
        queryset=User.objects.all()
    )

    owner = serializers.SlugRelatedField(
        slug_field='username',
        queryset = User.objects.all()
    )

    url = serializers.HyperlinkedIdentityField(
        view_name = 'dropbox:detailview',
        lookup_field='pk'
    )

    # url = serializers.SerializerMethodField()

    class Meta:
        model= SecureFile
        fields = [
            'url',
            'owner',
            'shared_with',
            'content',
            'is_locked',
            'is_public',
        ]

    # this is another method of get this url, the manual way to enable customizations

    # def get_url(self, obj):
        # request = self.context.get("request")
        # if request is None:
            # return None
        # else:
            # return reverse("detailview", kwargs={'pk' : obj.id}, request=request) 