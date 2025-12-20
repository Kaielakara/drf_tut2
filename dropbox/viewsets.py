from rest_framework import permissions,viewsets


from .models import SecureFile
from .serializers import SecureFileSerializers
from .permissions import IsValidPerson

class SecureViewSet(viewsets.ModelViewSet):
    queryset = SecureFile.objects.all()
    serializer_class = SecureFileSerializers
    permission_classes = [IsValidPerson, permissions.IsAuthenticated]

