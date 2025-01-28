from django.db import models
from django.urls import reverse


# Create your models here.
class Booking(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateTimeField()

    class Meta:
        ordering = ["bookingdate"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # for url paths that appear in templates
        return reverse("booking_detail", kwargs={"pk": self.pk})


class Menu(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} : {str(self.price)}"

    def get_absolute_url(self):
        # for url paths that appear in templates
        return reverse("menu_detail", kwargs={"pk": self.pk})
