from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from littlelemon.models import Menu

class MenuViewTest(TestCase):

    def setUp(self):
        # Setup runs before every test method
        Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_all_menu_items(self):
        url = reverse('menu-list-create')  # replace 'name_of_your_menu_list_url' with the actual name of your Menu list URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
