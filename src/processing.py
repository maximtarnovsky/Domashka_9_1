def filter_by_state(list_data: list, key: str = "EXECUTED") -> list:
    """Функция, принимающая список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'), и возвращающая новый список словарей, содержащий
    только те словари, у которых ключ state соответствует указанному значению."""
    new_list = []
    for i in list_data:
        if i["state"] == key:
            new_list.append(i)
    return new_list


def sort_by_date(sorted_list: list, reverse: bool = True) -> list:
    """Функция, принимающая список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание), и возвращающая новый список, отсортированный по дате (date)."""
    return sorted(sorted_list, key=lambda x: x["date"], reverse=reverse)
