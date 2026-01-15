"""Example script for demonstrating the debug_get_call_chain tool.

This script has a clear call hierarchy that's perfect for visualizing
how the call chain tool shows the path from entry point to current location.

Suggested debugging prompt for your AI agent:
---------------------------------------------
Debug examples/call_hierarchy_demo.py and set a breakpoint at line 46
(inside calculate_discount). When it pauses, use debug_get_call_chain
with format="tui" to see the complete call hierarchy with source context
showing how we got there.

The call chain will show:
  main() -> process_order() -> apply_pricing() -> calculate_discount()

Each frame will include the surrounding source code so you can understand
the context of each call.
"""


def calculate_discount(base_price: float, customer_tier: str) -> float:
    """Calculate discount based on customer tier.

    Args:
        base_price: Original price before discount
        customer_tier: Customer loyalty tier (bronze/silver/gold/platinum)

    Returns:
        Discount amount to subtract from base_price
    """
    discount_rates = {
        "bronze": 0.05,
        "silver": 0.10,
        "gold": 0.15,
        "platinum": 0.20,
    }

    rate = discount_rates.get(customer_tier, 0.0)
    discount = base_price * rate

    # Set breakpoint here (line 46) to see the full call chain
    print(f"Applying {rate:.0%} discount: ${discount:.2f}")  # Line 46

    return discount


def apply_pricing(items: list[dict], customer_tier: str) -> dict:
    """Apply pricing rules including discounts.

    Args:
        items: List of order items with 'name' and 'price'
        customer_tier: Customer loyalty tier

    Returns:
        Pricing breakdown with subtotal, discount, and total
    """
    subtotal = sum(item["price"] for item in items)
    discount = calculate_discount(subtotal, customer_tier)
    total = subtotal - discount

    return {
        "subtotal": subtotal,
        "discount": discount,
        "total": total,
    }


def process_order(order: dict) -> dict:
    """Process a customer order.

    Args:
        order: Order dict with 'customer', 'tier', and 'items'

    Returns:
        Processed order with pricing information
    """
    print(f"Processing order for {order['customer']}...")

    pricing = apply_pricing(order["items"], order["tier"])

    return {
        "customer": order["customer"],
        "tier": order["tier"],
        "items": order["items"],
        "pricing": pricing,
    }


def main():
    """Main entry point - creates and processes a sample order."""
    print("Call Hierarchy Demo")
    print("=" * 50)

    # Sample order data
    order = {
        "customer": "Alice Johnson",
        "tier": "gold",
        "items": [
            {"name": "Widget Pro", "price": 99.99},
            {"name": "Gadget Plus", "price": 149.99},
            {"name": "Accessory Pack", "price": 29.99},
        ],
    }

    print(f"\nCustomer: {order['customer']} ({order['tier']} tier)")
    print(f"Items: {len(order['items'])}")
    print()

    # Process the order - this will trigger our call chain
    result = process_order(order)

    # Display results
    print()
    print("Order Summary:")
    print(f"  Subtotal: ${result['pricing']['subtotal']:.2f}")
    print(f"  Discount: -${result['pricing']['discount']:.2f}")
    print(f"  Total:    ${result['pricing']['total']:.2f}")

    return result


if __name__ == "__main__":
    result = main()
