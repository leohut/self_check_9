"""
 Є список name з іменами користувачів, але всі починаються з малої літери.

name = ["dan", "jane", "steve", "mike"]
Розробіть функцію normal_name, яка приймає список імен та повертає теж список імен, але вже з правильними іменами з великої літери.

['Dan', 'Jane', 'Steve', 'Mike']
Необхідно використовувати функцію map. Не забудьте, що необхідно виконати перетворення типів для map.
 
	
 """
 
def normal_name(names):
    return list(map(str.capitalize, names))

# Приклад використання:
name = ["dan", "jane", "steve", "mike"]
result = normal_name(name)
print(result)
