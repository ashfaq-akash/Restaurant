from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet


from django.contrib.auth.models import User

from .models import Booking,Menu

from .serializers import BookingSerializer,MenuSerializer,UserSerializer


# Create your views here.
def index(request):
    return render(request,'index.html',{})


class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer