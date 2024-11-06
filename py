
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount to the price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price
