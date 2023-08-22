#define URL route for index() view
from django.urls import path
from . import views
from .views import UserView

urlpatterns = [
    path('', views.index, name='index'),
    #path('users/',UserView.as_view()),
    path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
]