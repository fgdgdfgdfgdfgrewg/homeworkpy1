## Модуль generators

### Примеры использования

**1. Фильтрация транзакций по валюте:**
```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
2. Получение описаний транзакций:

python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
3. Генерация номеров карт:

python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
text

### Шаг 4: Проверка качества кода
1. **Тестирование:**
   ```bash
   pytest --cov=src --cov-report=html
Убедитесь, что покрытие > 80%. Отчет будет в папке htmlcov.

Линтинг:

bash
flake8 src  # Проверка стиля (максимум 5 ошибок)
isort src    # Форматирование импортов