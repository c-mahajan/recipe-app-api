from django.test import TestCase

from app.calc import add
from app.calc import subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test That Two numbers are added togather"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test That values are subtracted and returned """
        self.assertEqual(subtract(5, 11), 6)
