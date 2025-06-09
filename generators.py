# src/generators.py

def filter_by_currency(transactions: list, currency: str) -> iter:
    """
    Возвращает итератор транзакций с заданной валютой.

    :param transactions: Список транзакций (словарей)
    :param currency: Код валюты (например, "USD")
    :yield: Транзакции с указанной валютой
    """
    for transaction in transactions:
        operation_amount = transaction["operationAmount"]
        currency_info = operation_amount["currency"]
        if currency_info["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> iter:
    """
    Генератор описаний транзакций.

    :param transactions: Список транзакций (словарей)
    :yield: Описание транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> iter:
    """
    Генератор номеров банковских карт в диапазоне [start, end].

    :param start: Начальный номер
    :param end: Конечный номер (включительно)
    :yield: Номер карты в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        num_str = f"{num:016d}"
        card_parts = [
            num_str[0:4],
            num_str[4:8],
            num_str[8:12],
            num_str[12:16]
        ]
        yield " ".join(card_parts)
