"""
This module provides a function to calculate a discounted price
based on the original price and the discount percentage.
"""


def calculate_discount(original_price: float, discount_percentage: float) -> float:
    """
    Calculate the discounted price given an original price and a discount percentage.

    Args:
        original_price (float): The original price of the item. Must be a non-negative number.
        discount_percentage (float): The discount percentage we want to apply. Must be between 0 and 100.

    Returns:
        float: The price after applying the discount.

    Raises:
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
    # Validate the input to ensure the original price is non-negative
    if not isinstance(original_price, (int, float)) or original_price < 0:
        raise ValueError("Original price must be a non-negative number.")

    # Validate the input to ensure the discount percentage is a number between 0 and 100
    if not isinstance(discount_percentage, (int, float)) or not (
        0 <= discount_percentage <= 100
    ):
        raise ValueError("Discount percentage must be a number between 0 and 100.")

    #  Apply the discount to the original price
    return original_price * (1 - discount_percentage / 100)
