from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer


# Create your views here.
def index(request):
    return render(request, "index.html", {})


class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serialized_items = bookingSerializer(items, many=True)
        return Response(serialized_items.data)

    def post(self, request):
        serializer = bookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})

class menuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serialized_items = menuSerializer(items, many=True)
        return Response(serialized_items.data)

    def post(self, request):
        serializer = menuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})