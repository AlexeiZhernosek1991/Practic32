# Задание 2

# Задача 1 вывести строку без знаков препинания
string_ = 'Что это было?... Я не ожидал увидеть подобного, но мне придется принять решение'
new_string1 = ''
for i in string_:
    if i.isalpha() or i.isspace():
        new_string1 += i
print(new_string1)

# Задача 2 вывести строку без букв верхнего регистра
new_string2 = ''
for i in string_:
    if i.isupper():
        pass
    else:
        new_string2 += i
print(new_string2)

# Задача 3 вывести всю строку в верхнем регистре
print(string_.upper())

# Задача 4 вывести строку изменив регистр букв с верхнего на нижний и на оборот
new_string2 = ''
for i in string_:
    if i.isupper():
        new_string2 += i.lower()
    elif i.islower():
        new_string2 += i.upper()
    else:
        new_string2 += i
print(new_string2)

# Задача 5 вывести строку заменив все знаки препинания на пробел
new_string5 = ''
for i in string_:
    if i.isalpha() or i.isspace():
        new_string5 += i
    else:
        new_string5 += ' '
print(new_string5)
