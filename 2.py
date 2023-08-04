"""
 Реалізуйте функцію get_discount_price_customer для розрахунку ціни на товар інтернет-магазину з урахуванням знижки клієнта.

Функція приймає два параметри:

price — ціна продукту
customer — словник з даними клієнта такого виду: {"name": "Dima"} або {"name": "Boris", "discount": 0.15}
Ви маєте глобальну змінну DEFAULT_DISCOUNT, яка визначає знижку для клієнта, якщо у нього немає поля discount.

Функція get_discount_price_customer має повертати нову ціну товару для клієнта.

Нагадаємо, що дисконт discount - це дробове число від 0 до 1. І ми під знижкою розуміємо коефіцієнт, який визначає величину ціни. 
І на цю величину ми знижуємо підсумкову ціну товару: price = price * (1 - discount).
 
"""
 
DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    # Перевірка наявності ключа 'discount' в словнику customer
    if 'discount' in customer:
        discount = customer['discount']
    else:
        discount = DEFAULT_DISCOUNT

    # Розрахунок ціни з урахуванням знижки
    discounted_price = price * (1 - discount)

    return discounted_price

# Приклад використання функції:
# Знижка для клієнта "Dima" відсутня, використовується знижка за замовчуванням
customer_dima = {"name": "Dima"}
price_product = 1000
discounted_price_dima = get_discount_price_customer(price_product, customer_dima)
print("Ціна товару для клієнта 'Dima':", discounted_price_dima)

# Знижка для клієнта "Boris" становить 15%
customer_boris = {"name": "Boris", "discount": 0.15}
discounted_price_boris = get_discount_price_customer(price_product, customer_boris)
print("Ціна товару для клієнта 'Boris':", discounted_price_boris)