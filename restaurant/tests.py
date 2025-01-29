from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer


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
class MenuViewTest(APITestCase):
    @classmethod
    def setUp(self):

        self.menu_url = reverse("menu_list")
        self.user = User.objects.create_user(
            username="testadmin", password="testpassword789"
        )
        self.item1 = Menu.objects.create(
            title="Test food item 1",
            price=5,
            inventory=1,
        )
        self.item2 = Menu.objects.create(
            title="Test food item 2",
            price=6.5,
            inventory=2,
        )
        self.item3 = Menu.objects.create(
            title="Test food item 3",
            price=7.25,
            inventory=3,
        )

    def test_menu_listview(self):
        self.client.login(username="testadmin", password="testpassword789")
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, 200)

        serialized_items = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.data, serialized_items.data)
        self.assertEqual(len(response.data), 3)

    def test_menu_create(self):
        self.client.login(username="testadmin", password="testpassword789")
        item = {"title": "Test food item 4", "price": 8, "inventory": 4}
        response = self.client.post(self.menu_url, item, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)


# Booking
class BookingViewTest(APITestCase):
    @classmethod
    def setUp(self):
        self.booking_url = reverse("booking_list")
        self.user = User.objects.create_user(
            username="testadmin", password="testpassword789"
        )
        self.booking1 = Booking.objects.create(
            name="John",
            no_of_guests=1,
            bookingdate="2026-01-29T12:00:00-05:00",
        )
        self.booking2 = Booking.objects.create(
            name="Jane",
            no_of_guests=1,
            bookingdate="2026-01-29T13:00:00-05:00",
        )
        self.booking3 = Booking.objects.create(
            name="Misha",
            no_of_guests=1,
            bookingdate="2026-01-29T14:00:00-05:00",
        )

    def test_booking_listview(self):
        self.client.login(username="testadmin", password="testpassword789")
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, 200)
        serialized_items = BookingSerializer(Booking.objects.all(), many=True)

        self.assertEqual(response.data, serialized_items.data)
        self.assertEqual(len(response.data), 3)

    def test_booking_create(self):
        self.client.login(username="testadmin", password="testpassword789")
        booking = {
            "name": "Sana",
            "no_of_guests": 1,
            "bookingdate": "2026-01-29T16:00:00-05:00",
        }
        response = self.client.post(self.booking_url, booking, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 4)
