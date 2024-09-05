def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    digit_count = 0
    for i in card_number:
        if i.isdigit():
            digit_count += 1
    if digit_count != 16:
        return "Ошибка ввода"
    else:
        return f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    digit_count = 0
    for i in account_number:
        if i.isdigit():
            digit_count += 1
    if digit_count != 20:
        return "Ошибка ввода"
    elif len(account_number) > 20:
        return f"{account_number[:5]}**{account_number[-4:]}"
    else:
        return f"**{account_number[-4:]}"
