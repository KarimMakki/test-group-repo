"""
Unit tests for the calculate_discount function.
"""

import unittest

from ..calculate_discount import calculate_discount


class TestCalculateDiscount(unittest.TestCase):
    """
    Tests for the calculate_discount function.
    """

    def test_valid_discount(self):
        """Test with a valid discount percentage."""
        self.assertEqual(calculate_discount(100, 20), 80.0)

    def test_no_discount(self):
        """Test with a discount percentage of 0."""
        self.assertEqual(calculate_discount(50, 0), 50.0)

    def test_full_discount(self):
        """Test with a discount percentage of 100."""
        self.assertEqual(calculate_discount(200, 100), 0.0)

    def test_negative_price(self):
        """Test with a negative original price."""
        with self.assertRaises(ValueError):
            calculate_discount(-50, 20)

    def test_discount_below_zero(self):
        """Test with a discount percentage below 0."""
        with self.assertRaises(ValueError):
            calculate_discount(50, -10)

    def test_discount_above_hundred(self):
        """Test with a discount percentage above 100."""
        with self.assertRaises(ValueError):
            calculate_discount(50, 150)

    def test_non_numeric_price(self):
        """Test with a non-numeric original price."""
        with self.assertRaises(ValueError):
            calculate_discount("100", 20)

    def test_non_numeric_discount(self):
        """Test with a non-numeric discount percentage."""
        with self.assertRaises(ValueError):
            calculate_discount(100, "20")
