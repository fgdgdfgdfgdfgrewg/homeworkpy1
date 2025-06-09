# src/generators.py

def filter_by_currency(transactions: list, currency: str) -> iter:
    """
    Возвращает итератор транзакций с заданной валютой.

    :param transactions: Список транзакций (словарей)
    :param currency: Код валюты (например, "USD")
    :yield: Транзакции с указанной валютой
    """
    for transaction in transactions:
        operation_currency = transaction["operationAmount"]["currency"]["code"]
        if operation_currency == currency:
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
        num_str = f"{num:016d}"  # Форматируем в 16-значное число с ведущими нулями
        yield " ".join([num_str[i:i + 4] for i in range(0, 16, 4))
