from rest_framework import viewsets
from shop.permissions import IsManagerPermission, IsCustomerPermission

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = []
        else:
            permission_classes = [IsManagerPermission()]
        return permission_classes
