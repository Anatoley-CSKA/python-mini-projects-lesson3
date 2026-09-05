def get_mask_card_number(card_number: str) -> str:
    """Return masked card number."""
    if not card_number or len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Card number must contain 16 digits")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
