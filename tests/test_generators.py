# import pytest
#
# from src.generators import card_number_generator
# from src.generators import filter_by_currency
# from src.generators import transaction_descriptions


# Юля Нафикова

from sys import exc_info

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_filter_by_currency_usd():
    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_rub():
    generator = filter_by_currency(transactions, "rub")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_zero():
    generator = filter_by_currency([], "")
    assert next(generator) == "Нет транзакций"


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_zero():
    generator = transaction_descriptions([])
    assert next(generator) == "Нет транзакций"


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"


# @pytest.fixture
# def transactions() -> list:
#     return [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {
#                     "amount": "79114.93",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188"
#             },
#             {
#                 "id": 873106923,
#                 "state": "EXECUTED",
#                 "date": "2019-03-23T01:09:46.296404",
#                 "operationAmount": {
#                     "amount": "43318.34",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод со счета на счет",
#                 "from": "Счет 44812258784861134719",
#                 "to": "Счет 74489636417521191160"
#             },
#             {
#                 "id": 895315941,
#                 "state": "EXECUTED",
#                 "date": "2018-08-19T04:27:37.904916",
#                 "operationAmount": {
#                     "amount": "56883.54",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод с карты на карту",
#                 "from": "Visa Classic 6831982476737658",
#                 "to": "Visa Platinum 8990922113665229"
#             },
#             {
#                 "id": 594226727,
#                 "state": "CANCELED",
#                 "date": "2018-09-12T21:27:25.241689",
#                 "operationAmount": {
#                     "amount": "67314.70",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Visa Platinum 1246377376343588",
#                 "to": "Счет 14211924144426031657"
#             }]
#
#
# def test_filter_by_currency(transactions: list) -> None:
#     assert filter_by_currency(transactions, )
#
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(3):
#     print(next(usd_transactions))
#
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
# {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
# {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}
#
#
#
#
#
# # Тестирование функции filter_by_currency
# def test_filter_by_currency(transactions: list[dict]) -> None:
#     result = filter_by_currency(transactions, "USD")
#     assert next(result) == {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     }
#     assert next(result) == {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     }
#     assert next(result) == {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     }
#     with pytest.raises(StopIteration):
#         next(result)

#
# def test_filter_by_currency_not_currency(transactions: list[dict]) -> None:
#     generator = filter_by_currency(transactions, "EUR")
#     assert list(generator) == []
#
#
# def test_filter_by_currency_empty(transactions: list[dict]) -> None:
#     with pytest.raises(TypeError):
#         filter_by_currency([], "EUR")
#

# # Тестирование функции transaction_descriptions
# def test_transaction_descriptions(transactions: list[dict]) -> None:
#     descriptions = transaction_descriptions(transactions)
#     assert next(descriptions) == "Перевод организации"
#     assert next(descriptions) == "Перевод со счета на счет"
#     assert next(descriptions) == "Перевод со счета на счет"
#     assert next(descriptions) == "Перевод с карты на карту"
#     assert next(descriptions) == "Перевод организации"
#
#
# def test_transaction_descriptions_empty(transactions: list[dict]) -> None:
#     descriptions = transaction_descriptions([])
#     assert list(descriptions) == []
#
#
# # Тестирование функции card_number_generator
# @pytest.mark.parametrize(
#     "start, stop, expected",
#     [
#         (0, 1, "0000 0000 0000 0000"),
#         (9999999999999999, 9999999999999999, "9999 9999 9999 9999"),
#         (1000, 1001, "0000 0000 0000 1000"),
#     ],
# )
# def test_card_number_generator(start: int, stop: int, expected: str) -> None:
#     generated_number = card_number_generator(start, stop)
#     assert next(generated_number) == expected
#
#
# def test_card_number_generator_range(start: int = 1, stop: int = 5) -> None:
#     generated_number = card_number_generator(1, 5)
#     assert next(generated_number) == "0000 0000 0000 0001"
#     assert next(generated_number) == "0000 0000 0000 0002"
#     assert next(generated_number) == "0000 0000 0000 0003"
#     assert next(generated_number) == "0000 0000 0000 0004"
#     assert next(generated_number) == "0000 0000 0000 0005"


#
# def test_filter_by_currency_empty(transactions):
#     with pytest.raises(ValueError):
#         assert filter_by_currency([], "EUR") == "Ввели пустой список!"