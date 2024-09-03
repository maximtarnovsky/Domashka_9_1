# import pytest
#
# from src.processing import filter_by_state, sort_by_date
#
#
# @pytest.fixture
# def dict_test() -> list:
#     return [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 615064591, "state": "ZZZZZZZZ", "date": "2018-10-13T08:21:33.419441"},
#     ]
#
#
# def test_filter_by_state(dict_test: list) -> None:
#     """Тестирования функции filter_by_state для фильтрации словарей по заданному статусу"""
#     assert filter_by_state(dict_test) == [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     ]
#
#     assert filter_by_state(dict_test, key="CANCELED") == [
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
#
#     assert filter_by_state(dict_test * 0) == []
#
#
# def test_sort_by_date(dict_test: list) -> None:
#     """Тестирование функции sort_by_date для сортировки списка словарей по датам"""
#     assert sort_by_date(dict_test) == [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 615064591, "state": "ZZZZZZZZ", "date": "2018-10-13T08:21:33.419441"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     ]
#
#     assert sort_by_date(dict_test, reverse=False) == [
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "ZZZZZZZZ", "date": "2018-10-13T08:21:33.419441"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     ]
