from django.test import TestCase

from littlelemon.LittleLemonAPI.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCreams : 80")

