import math


# Задание 1
# задача №1 рекурсивная функция факториал числа n

def fact(n):
    if n == 1:
        return n
    elif n != 1:
        return n * fact(n - 1)


print(fact(4), math.factorial(4))


# задача №2 функция возвращает последовательность фиббоначи в заданном диапозоне от 0=n

# задача №2 вариант первый
def fib1(n):
    if n in (1, 2):
        return 1
    else:
        return fib1(n - 2) + fib1(n - 1)


# задача №2 вариант второй
def fib2(n):
    list1 = [0, 1]
    for x in range(n - 1):
        s = list1[-1] + list1[-2]
        list1.append(s)
    return list1[-1], list1


print(fib1(10))
print(fib2(10))

# задача №3
dict_1 = {
    'верный': [11, 55.2, 'слон'],
    'фиолетовый': 15,
    'орда': 'восемь'
}
dict_2 = {
    'ода': {52, 99, 2},
    'сороконожка': {110, 'слово', 15}
}

list_3 = list(dict_1.keys()) + list(dict_2.keys())
list_3.sort(key=len)
dict_3 = {}
for x in list_3:
    if x in dict_1:
        dict_3.setdefault(x, dict_1.get(x))
    elif x in dict_2:
        dict_3.setdefault(x, dict_2.get(x))
print(dict_3)
