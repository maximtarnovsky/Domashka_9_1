import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("", "Ошибка ввода"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(numbers: str, expected: str) -> None:
    """Тестирование корректности работы функции mask_account_card"""
    assert mask_account_card(numbers) == expected


@pytest.mark.parametrize(
    "uncleared_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("24-03-11T02:26:18.671407", "Ошибка ввода"),
        ("2024-9-11T02:26:18.671407", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_get_date(uncleared_date: str, expected: str) -> None:
    """Тестирования корректности работы функции get_date"""
    assert get_date(uncleared_date) == expected
