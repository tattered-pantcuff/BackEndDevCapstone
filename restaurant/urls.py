from django.urls import path


from .views import MenuItemView, SingleMenuItemView, BookingView, SingleBookingView

urlpatterns = [
    path("menu/", MenuItemView.as_view(), name="menu_list"),
    path("menu/<int:pk>", SingleMenuItemView.as_view(), name="menu_detail"),
    path("booking/", BookingView.as_view(), name="booking_list"),
    path("booking/<int:pk>", SingleBookingView.as_view(), name="booking_detail"),
]
