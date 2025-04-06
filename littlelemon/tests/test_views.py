from django.test import TestCase

from littlelemon.LittleLemonAPI.models import MenuItem
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from littlelemon.LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Pizza", price=120, inventory=50)
        self.item2 = MenuItem.objects.create(title="Burger", price=60, inventory=30)
        self.item3 = MenuItem.objects.create(title="Pasta", price=90, inventory=20)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)