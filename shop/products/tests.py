from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.factories import ProductFactory
from category.models import Category
from rest_framework_simplejwt.tokens import RefreshToken


class BaseProductAPITestCase(APITestCase):
    def setUp(self):
        self.user = self.create_user()
        self.products = ProductFactory.create_batch(3)
        self.category = Category.objects.create(name='Category', slug='category')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.get_jwt_token())

    def create_user(self):
        raise NotImplementedError("Subclasses must implement create_user method")

    def get_jwt_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)


class CustomerProductAPITestCase(BaseProductAPITestCase):
    def create_user(self):
        return get_user_model().objects.create_user(
            username='customer',
            password='password',
            email='customer@email.com',
            role='customer'
        )

    def test_customer_can_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_can_get_product_detail(self):
        url = reverse('product-detail', args=[self.products[0].id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_cannot_create_product(self):
        url = reverse('product-list')
        data = {'name': 'New Product', 'price': 20.0}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cannot_update_product(self):
        url = reverse('product-detail', args=[self.products[1].id])
        data = {'name': 'Updated Product', 'price': 15.0}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_customer_cannot_delete_product(self):
        url = reverse('product-detail', args=[self.products[2].id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ManagerProductAPITestCase(BaseProductAPITestCase):
    def create_user(self):
        return get_user_model().objects.create_user(
            username='manager',
            password='password',
            email='manager@email.com',
            role='manager'
        )

    def test_manager_can_create_product(self):
        url = reverse('product-list')
        data = {
            'title': 'New Product',
            'description': 'New Product Description',
            'price': 20,
            'discount': 50,
            'category': self.category.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_manager_can_update_product(self):
        url = reverse('product-detail', args=[self.products[1].id])
        data = {'title': 'Updated Product', 'price': '15.0'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_manager_can_delete_product(self):
        url = reverse('product-detail', args=[self.products[2].id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
