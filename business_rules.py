# business_rules.py
# Author: Yusra Batool

SHORT_RENTAL_LIMIT = 3
LONG_RENTAL_LIMIT = 7

STANDARD_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20
CONTRACTOR_DISCOUNT = 0.10

DAMAGE_WAIVER = 25.00
WAIVER_THRESHOLD = 150.00
DEPOSIT_THRESHOLD = 1000.00
INSPECTION_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00

def calculate_rental_cost(daily_rate: float, days: int) -> float:
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the applicable rental discount rate."""
    if days >= LONG_RENTAL_LIMIT:
        discount = LONG_RENTAL_DISCOUNT
    elif days >= SHORT_RENTAL_LIMIT:
        discount = STANDARD_DISCOUNT
    else:
        discount = 0.0

    if contractor and discount < CONTRACTOR_DISCOUNT:
        discount = CONTRACTOR_DISCOUNT

    return discount

def calculate_quote(
    daily_rate: float, days: int, contractor: bool = False) -> float:
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)

    discounted_cost = cost * (1 - discount)

    if discounted_cost < WAIVER_THRESHOLD:
        discounted_cost += DAMAGE_WAIVER

    return round(discounted_cost, 2)

def requires_deposit(quote: float) -> bool:
    return quote >= DEPOSIT_THRESHOLD

def needs_inspection(days: int, quote: float) -> bool:
    return (
        days >= INSPECTION_DAYS
        and quote > INSPECTION_QUOTE_THRESHOLD
    )


def total_quoted(rentals: list) -> float:
    total = 0.0

    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"],
            rental["days"],
            rental["contractor"]
        )

    return total


def largest_rental(rentals: list) -> str:
    largest_customer = ""
    largest_quote = -1.0

    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"],
            rental["days"],
            rental["contractor"]
        )

        if quote > largest_quote:
            largest_quote = quote
            largest_customer = rental["customer"]

    return largest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    deposit_text = "yes" if deposit else "no"
    inspection_text = "yes" if inspection else "no"

    return (
        f"{customer}: ${quote:.2f} | "
        f"deposit: {deposit_text} | "
        f"inspection: {inspection_text}"
    )
