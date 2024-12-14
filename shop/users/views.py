from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from shop.permissions import IsAdminPermission, IsCustomerPermission
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['delete', 'update', 'list']:
            permission_classes.append(IsAdminPermission())
            permission_classes.append(IsAuthenticated())
        elif self.action == 'create':
            pass
        return permission_classes

    def get_queryset(self):
        role = self.request.query_params.get('role')
        if role:
            return self.queryset.filter(role=role)
        return self.queryset

