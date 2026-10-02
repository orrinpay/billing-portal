from decimal import Decimal

from orrin_billing.pricing import total_with_tax


def test_total_with_tax() -> None:
    assert total_with_tax(Decimal("100")) == Decimal("123.00")
