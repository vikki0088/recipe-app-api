"""
simple tests
"""

from django.test import SimpleTestCase
from app import calc

class ClacTests(SimpleTestCase):
    """
    test for calc
    """
    def test_add_numbers(self):
        res = calc.add(3,5)
        self.assertEqual(res,8)

    def test_sub_numbers(self):
        res = calc.sub(10,15)
        self.assertEqual(res,5)


