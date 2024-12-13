from rest_framework import viewsets
from .serializers import OrderModelSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
	serializer_class = OrderModelSerializer
	queryset = Order.objects.all()
