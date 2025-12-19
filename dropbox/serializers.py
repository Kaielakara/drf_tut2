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

    class Meta:
        model= SecureFile
        fields = [
            'id',
            'owner',
            'shared_with',
            'content',
            'is_locked',
            'is_public',
        ]