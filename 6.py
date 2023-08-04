"""
 Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,

"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, 
який буде віддавати зазначені числа при зверненні до нього у циклі.

З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.
 
"""

import re

def generator_numbers(string=""):
    # Знайдемо всі цілі числа в рядку за допомогою регулярного виразу
    numbers = re.findall(r'\d+', string)
    
    # Повертаємо числа по одному в циклі з допомогою yield
    for number in numbers:
        yield int(number)

def sum_profit(string):
    # Створюємо генератор чисел зі строки
    numbers_generator = generator_numbers(string)
    
    # Ініціалізуємо зміну для підсумовування чисел
    total_profit = 0
    
    # Перебираємо числа, отримані від генератора, та додаємо їх до загальної суми
    for number in numbers_generator:
        total_profit += number
        
    # Повертаємо загальний прибуток
    return total_profit

# Приклад використання:
input_string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
total_profit = sum_profit(input_string)
print("Total profit:", total_profit)