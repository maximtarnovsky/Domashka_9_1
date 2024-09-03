from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(numbers: str) -> str:
    """Обработка и маскировка информации о картах и счетах"""
    digit_count = 0
    for i in numbers:
        if i.isdigit():
            digit_count += 1
    if digit_count == 20:
        return get_mask_account(numbers)
    elif digit_count == 16:
        return get_mask_card_number(numbers)
    else:
        return "Ошибка ввода"


def get_date(uncleared_date: str) -> str:
    """Приведение даты к формату ДД.ММ.ГГГГ"""
    if not uncleared_date[8:10].isdigit():
        return "Ошибка ввода"
    elif not uncleared_date[5:7].isdigit():
        return "Ошибка ввода"
    elif not uncleared_date[:4].isdigit():
        return "Ошибка ввода"
    else:
        return f"{uncleared_date[8:10]}.{uncleared_date[5:7]}.{uncleared_date[:4]}"
