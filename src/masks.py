def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    return f"{account_number[:5]}**{account_number[-4:]}"
