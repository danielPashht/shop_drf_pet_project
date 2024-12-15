from rest_framework import viewsets
from shop.permissions import IsOwnerPermission

from .models import Cart
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwnerPermission]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user).first()
