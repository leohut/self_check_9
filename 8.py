"""
 Є список contacts, елементи якого - словники контактів наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Розробіть функцію get_emails, яка отримує у параметрі список list_contacts та повертає список, 
який містить електронні адреси всіх контактів зі списку list_contacts. 
Використовуйте функцію map.
 
"""


def get_emails(list_contacts):
    # Визначаємо функцію, яка приймає словник контакту і повертає email
    def get_email(contact):
        return contact["email"]

    # Використовуємо map для виклику функції get_email для кожного контакту у списку
    emails_iterator = map(get_email, list_contacts)

    # Перетворюємо ітератор у звичайний список і повертаємо його
    emails_list = list(emails_iterator)
    return emails_list

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
    # Додайте інші контакти, якщо є
]

emails_list = get_emails(contacts)
print(emails_list)