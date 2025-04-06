from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu, Booking
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# filepath: d:\coursera\main project\littlelemon\workspace\littlelemon\restaurant\test_test.py

class MenuModelTestCase(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="Pizza", price=12.99, inventory=10)

    def test_menu_str(self):
        self.assertEqual(str(self.menu_item), "Pizza - $12.99")

class BookingModelTestCase(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(name="John Doe", no_of_guests=4, booking_date="2023-10-10T18:00:00Z")

    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John Doe - 2023-10-10T18:00:00Z")

class MenuItemsViewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.menu_item = Menu.objects.create(title="Burger", price=8.99, inventory=20)
        self.list_url = reverse('menu_items') 
        self.detail_url = reverse('single_menu_item', args=[self.menu_item.id]) 

    def test_get_menu_items(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        data = {"title": "Pasta", "price": 10.99, "inventory": 15}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_menu_item(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_menu_item(self):
        data = {"title": "Updated Burger", "price": 9.99, "inventory": 25}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_menu_item(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookingViewSetTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.booking = Booking.objects.create(name="Jane Doe", no_of_guests=2, booking_date="2023-10-15T19:00:00Z")
        self.list_url = "/restaurant/booking/tables/"  
        self.detail_url = "/restaurant/booking/tables/"  + str(self.booking.id) +"/"

    def test_get_bookings(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        data = {"name": "Alice", "no_of_guests": 3, "booking_date": "2023-10-20T20:00:00Z"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_single_booking(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_booking(self):
        data = {"name": "Updated Jane", "no_of_guests": 4, "booking_date": "2023-10-16T19:00:00Z"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_booking(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)