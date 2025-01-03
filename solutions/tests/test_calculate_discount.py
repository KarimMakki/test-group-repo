#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides unit tests for the function calculate_discount.
Created on: 2025/1/2
@author: KarimMakki
"""

import unittest

from ..calculate_discount import calculate_discount


class TestCalculateDiscount(unittest.TestCase):
    """Unit tests for the calculate_discount function."""

    def test_valid_discount_case1(self):
        """Test valid input: original_price=100, discount_percentage=20."""
        self.assertEqual(calculate_discount(100, 20), 80.0)

    def test_valid_discount_case2(self):
        """Test valid input: original_price=50, discount_percentage=0."""
        self.assertEqual(calculate_discount(50, 0), 50.0)

    def test_valid_discount_case3(self):
        """Test valid input: original_price=200, discount_percentage=100."""
        self.assertEqual(calculate_discount(200, 100), 0.0)

    def test_invalid_type_original_price(self):
        """Test invalid type for original_price."""
        with self.assertRaises(AssertionError):
            calculate_discount("100", 20)

    def test_invalid_type_discount_percentage(self):
        """Test invalid type for discount_percentage."""
        with self.assertRaises(AssertionError):
            calculate_discount(100, "20")

    def test_negative_original_price(self):
        """Test negative original_price."""
        with self.assertRaises(ValueError):
            calculate_discount(-100, 20)

    def test_out_of_range_discount_percentage_low(self):
        """Test discount_percentage less than 0."""
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)

    def test_out_of_range_discount_percentage_high(self):
        """Test discount_percentage greater than 100."""
        with self.assertRaises(ValueError):
            calculate_discount(100, 110)
