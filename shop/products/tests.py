from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from products.models import Product
from products.factories import ProductFactory
from rest_framework_simplejwt.tokens import RefreshToken


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.customer = get_user_model().objects.create_user(
            username='customer',
            password='password',
            email='test@email.com',
            role='customer'
        )
        self.product = ProductFactory.create_batch(3)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_jwt_token())

    def get_jwt_token(self):
        refresh = RefreshToken.for_user(self.customer)
        return str(refresh.access_token)

    def test_customer_can_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_can_get_product_detail(self):
        url = reverse('product-detail', args=[self.product[0].id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_cannot_create_product(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'price': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cannot_update_product(self):
        url = reverse('product-detail', args=[self.product[1].id])
        data = {'name': 'Updated Product', 'price': 15.0}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cannot_delete_product(self):
        url = reverse('product-detail', args=[self.product[2].id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
