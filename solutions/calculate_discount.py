#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate a discounted price
based on the original price and the discount percentage.
Created on: 2025/1/2
@author: KarimMakki
"""


def calculate_discount(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price given an original price and a discount percentage.

    Arguments:
        original_price (float): The original price of the item. Must be a non-negative number.
        discount_percentage (float): The discount percentage to apply. Must be between 0 and 100.

    Returns:
        float: The price after applying the discount.

    Raises:
        AssertionError: original_price is not a number
        AssertionError: discount_percentage is not a number
        ValueError: If the original price is negative.
        ValueError: If the discount percentage is not between 0 and 100.

    Examples:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50, 0)
        50.0
        >>> calculate_discount(200, 100)
        0.0
    """
    # Assert that inputs are of the correct type
    assert isinstance(original_price, (int, float)), "Original price must be a number."
    assert isinstance(
        discount_percentage, (int, float)
    ), "Discount percentage must be a number."

    # Validate the input values
    if original_price < 0:
        raise ValueError("Original price must be a non-negative number.")
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Discount percentage must be between 0 and 100.")

    # make the discount factor
    discount_factor = 1 - discount_percentage / 100

    # Return the discounted price
    return original_price * discount_factor
