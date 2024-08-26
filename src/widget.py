# def mask_account_card(card_acount_number: str) -> str:
#     """Обработка и маскировка информации о счетах и картах"""
#
#     return f""
#

def get_date(uncleared_date: str) -> str:
    """Приведение даты к формату ДД.ММ.ГГГГ"""
    return f"{uncleared_date[8:10]}.{uncleared_date[5:7]}.{uncleared_date[:4]}"
