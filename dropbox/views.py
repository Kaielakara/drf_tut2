from django.shortcuts import render
from rest_framework import authentication, generics, permissions
from rest_framework.response import Response

from .authentication import TokenAutentication
from .models import SecureFile
from .permissions import IsValidPerson
from .serializers import SecureFileSerializers

# Create your views here.
class ContentListView(generics.ListAPIView):
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializers
    authentication_classes = [authentication.BasicAuthentication, authentication.SessionAuthentication, TokenAutentication]
    permission_classes = [permissions.IsAuthenticated]


class ContentCreateView(generics.CreateAPIView):
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):

        is_many = isinstance(request.data, list)

        serializer = self.get_serializer(data=request.data, many=is_many)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        
        return Response(serializer.data)
    
class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializers
    authentication_classes = [TokenAutentication]
    permission_classes = [permissions.IsAuthenticated, IsValidPerson]

