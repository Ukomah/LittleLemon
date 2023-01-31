from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(
            title="Pizza",
            price=15.99,
            inventory=10
        )
        MenuItem.objects.create(
            name="Burger",
            price=12.99,
            inventory=7
        )
        MenuItem.objects.create(
            name="Salad",
            price=9.99,
            inventory=19
        )
    
    def test_getall(self):
        menus = MenuItem.objects.all()
        serialized_data = MenuItemSerializer(menus, many=True).data
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_data, response.data)