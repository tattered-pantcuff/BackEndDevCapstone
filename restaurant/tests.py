from django.test import TestCase
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your tests here.


# Models
class MenuTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.menu = Menu.objects.create(
            title="Test food item",
            price=5,
            inventory=1,
        )

    def test_menu_model(self):
        self.assertEqual(self.menu.title, "Test food item")
        self.assertEqual(self.menu.price, 5)
        self.assertEqual(self.menu.inventory, 1)

        self.assertEqual(str(self.menu), "Test food item : 5")


class BookingTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.booking = Booking.objects.create(
            name="John",
            no_of_guests=2,
            bookingdate=timezone.now(),
        )

    def test_menu_model(self):

        self.assertEqual(self.booking.name, "John")
        self.assertEqual(self.booking.no_of_guests, 2)
        assert self.booking.bookingdate <= timezone.now()


# Views
class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.menu = Menu.objects.create(
            title="Test food item",
            price=5,
            inventory=1,
        )

    def test_menu_listview(self):

        response = self.client.get(reverse("menu_list"))
        item = Menu.objects.all()
        #serialized_item = MenuSerializer(item)
        self.assertContains(response, item)

# Write a MenuViewTest class that subclasses the TestCase class.

# Use the setup() method to add a few test instances of the Menu model.

# Next, add another test_getall() instance method to retrieve all the Menu objects added for the test purpose. 

# The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
