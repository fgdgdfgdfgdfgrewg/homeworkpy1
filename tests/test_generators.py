# tests/test_generators.py

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [...]  # Используйте пример транзакций из задания


# Тесты для filter_by_currency
@pytest.mark.parametrize("currency, expected_count", [("USD", 3), ("RUB", 2), ("EUR", 0)])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    filtered = list(filter_by_currency(sample_transactions, currency))
    assert len(filtered) == expected_count
    for transaction in filtered:
        assert transaction["operationAmount"]["currency"]["code"] == currency


def test_filter_empty_list():
    assert list(filter_by_currency([], "USD")) == []


# Тесты для transaction_descriptions
@pytest.mark.parametrize("index, expected", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод со счета на счет")
])
def test_transaction_descriptions(sample_transactions, index, expected):
    gen = transaction_descriptions(sample_transactions)
    for _ in range(index + 1):
        description = next(gen)
    assert description == expected


# Тесты для card_number_generator
@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999999999999999, 10000000000000000, ["9999 9999 9999 9999", "0000 0000 0000 0000"])
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected
