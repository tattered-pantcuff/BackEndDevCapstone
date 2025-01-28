from django.urls import path


from .views import MenuItemView, SingleMenuItemView, BookingView, SingleBookingView

urlpatterns = [
    path("menu/", MenuItemView.as_view()),
    path("menu/<int:pk>", SingleMenuItemView.as_view()),
    path("booking/", BookingView.as_view()),
    path("booking/<int:pk>", SingleBookingView.as_view()),
    
]
