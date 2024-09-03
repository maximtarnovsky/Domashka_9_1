# import pytest
#
# from src.masks import get_mask_account, get_mask_card_number
#
#
# @pytest.mark.parametrize(
#     "card_numbers, expected",
#     [
#         ("7000792289606361", "7000 79** **** 6361"),
#         ("1234567890123456789", "Ошибка ввода"),
#         ("1234567890", "Ошибка ввода"),
#         ("", "Ошибка ввода"),
#         ("123456789012345a", "Ошибка ввода"),
#     ],
# )
# def test_get_mask_card_number(card_numbers: str, expected: str) -> None:
#     """Тестирование функции get_mask_card_number для маскировки номера карты"""
#     assert get_mask_card_number(card_numbers) == expected
#
#
# @pytest.mark.parametrize(
#     "account_numbers, expected",
#     [
#         ("73654108430135874305", "**4305"),
#         ("12345678901234567890123", "Ошибка ввода"),
#         ("1234567890", "Ошибка ввода"),
#         ("", "Ошибка ввода"),
#         ("1234567890123456789a", "Ошибка ввода"),
#     ],
# )
# def test_get_mask_account(account_numbers: str, expected: str) -> None:
#     """Тестирование функции get_mask_account для маскировки номера счёта"""
#     assert get_mask_account(account_numbers) == expected
