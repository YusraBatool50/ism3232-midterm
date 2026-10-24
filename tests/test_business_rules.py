# tests/test_business_rules.py
# Author: Yusra Batool

from business_rules import (
    calculate_rental_cost,
    get_rental_discount,
    calculate_quote,
    requires_deposit,
    needs_inspection,
    total_quoted,
    largest_rental,
    format_rental_line,
)

# test 1: calculate_rental_cost
def test_calculate_rental_cost_over_multiple_days():
    assert round(calculate_rental_cost(85.00, 4), 2) == 340.00

# test 2: get_rental_discount (testing limits)
def test_get_rental_discount_before_three_days():
    assert get_rental_discount(2) == 0.00


def test_get_rental_discount_at_three_days():
    assert get_rental_discount(3) == 0.10


def test_get_rental_discount_before_seven_days():
    assert get_rental_discount(6) == 0.10


def test_get_rental_discount_at_seven_days():
    assert get_rental_discount(7) == 0.20

# where passing contractor=True changes the answer
def test_get_rental_discount_contractor():
    assert get_rental_discount(2, True) == 0.10

# test 3: requires_deposit
def test_requires_deposit_below_limit():
    assert requires_deposit(999.99) is False


def test_requires_deposit_at_limit():
    assert requires_deposit(1000.00) is True

# test 4: needs_inspection
def test_needs_inspection_below_five_days():
    assert needs_inspection(4, 900.00) is False


def test_needs_inspection_at_five_days():
    assert needs_inspection(5, 900.00) is True


def test_needs_inspection_at_quote_limit():
    assert needs_inspection(5, 800.00) is False


def test_needs_inspection_above_quote_limit():
    assert needs_inspection(5, 800.01) is True

# test 5: total_quoted
def test_total_quoted_two_rentals():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    ]
    assert round(total_quoted(rentals), 2) == 278.00


def test_total_quoted_empty_list():
    assert round(total_quoted([]), 2) == 0.00

# test 6: format_rental_line

def test_format_rental_line_no_requirements():
    result = format_rental_line("Alvarez", 145.00, False, False)
    assert result == "Alvarez: $145.00 | deposit: no | inspection: no"


def test_format_rental_line_both_requirements():
    result = format_rental_line("Eastman", 1344.00, True, True)
    assert result == "Eastman: $1344.00 | deposit: yes | inspection: yes"

# test 7: largest_rental

def test_largest_rental_two_customers():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    ]
    assert largest_rental(rentals) == "Eastman"


def test_largest_rental_tie():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 100.00, "days": 4, "contractor": False},
        {"customer": "Brennan", "daily_rate": 100.00, "days": 4, "contractor": False},
    ]
    assert largest_rental(rentals) == "Alvarez"


def test_largest_rental_empty_list():
    assert largest_rental([]) == ""

# test 8: calculate_quote
def test_calculate_quote_below_waiver_limit():
    assert round(calculate_quote(149.99, 1), 2) == 174.99


def test_calculate_quote_at_waiver_limit():
    assert round(calculate_quote(150.00, 1), 2) == 150.00


def test_calculate_quote_with_discount():
    assert round(calculate_quote(85.00, 4), 2) == 306.00
