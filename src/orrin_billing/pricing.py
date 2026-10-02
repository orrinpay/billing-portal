from decimal import Decimal

TAX_RATE = Decimal("0.23")


def total_with_tax(net: Decimal) -> Decimal:
    if net < 0:
        raise ValueError("net must not be negative")
    return (net * (1 + TAX_RATE)).quantize(Decimal("0.01"))
