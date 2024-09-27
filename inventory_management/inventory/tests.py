from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Item

class ItemUpdateDeleteTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Obtain JWT token
        response = self.client.post(reverse('token_obtain_pair'), {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['access']
        
        # Set the token in the authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        # Create an item for testing
        self.item = Item.objects.create(name="Test Item", description="Test Description", quantity=10, price=99.99)
        self.url = reverse('item-detail', kwargs={'pk': self.item.id})

    def test_update_item(self):
        update_data = {"name": "Updated Item", "description": "Updated Description", "quantity": 20}
        response = self.client.put(self.url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Item")

    def test_partial_update_item(self):
        update_data = {"quantity": 25}
        response = self.client.patch(self.url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 25)

    def test_delete_item(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Item.objects.filter(pk=self.item.id).exists())
