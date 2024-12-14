from rest_framework import viewsets
from .models import Product
from shop.permissions import IsManagerPermission, IsCustomerPermission

from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsCustomerPermission]
        else:
            permission_classes = [IsManagerPermission]
