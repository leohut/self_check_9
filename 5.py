"""

 У модулі 5 ми написали функцію sanitize_phone_number для нормалізації рядка з телефонним номером. Нагадаємо, що при отриманні рядків

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
Ми отримували наступний вивід:

380501233234
0503451234
0508889900
380501112222
380501112211
Уявіть, що в іншому місці програми у нас виникла вимога зробити висновок у форматі

+380501233234
+380503451234
+380508889900
+380501112222
+380501112211
І тут ідеально підійде створення декоратора для функції sanitize_phone_number. 
Декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного номера (з 12 символом) - тільки знак +. 
Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.

 
"""

def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)  # Викликаємо оригінальну функцію sanitize_phone_number
        if len(new_phone) == 12:
            return "+" + new_phone
        else:
            return "+38" + new_phone
    return wrapper

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

# Приклад використання:
print(sanitize_phone_number("    +38(050)123-32-34"))  # Виведе: +380501233234
print(sanitize_phone_number("     0503451234"))  # Виведе: +380503451234
print(sanitize_phone_number("(050)8889900"))  # Виведе: +380508889900
print(sanitize_phone_number("38050-111-22-22"))  # Виведе: +380501112222
print(sanitize_phone_number("38050 111 22 11   "))  # Виведе: +380501112211