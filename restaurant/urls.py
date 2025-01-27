from django.urls import path

from .views import index, menuView, bookingView

urlpatterns = [
    path("", index, name="index"),
    path("menu/", menuView.as_view()),
    path("booking/", bookingView.as_view()),
]
