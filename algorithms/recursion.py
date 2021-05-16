#Рекурсивный подсчет факториала
def factorial(number):
    if number < 2:
        return number
    return number * factorial(number - 1)

print(factorial(3))


#Рекурсивное нахождение суммы элементов в массиве
def summ(array):
    if not array:
        return 0
    return array[0] + summ(array[1:])

print(summ([4, 5, 7, 3, 8]))


#Рекурсивный подсчет количества элементов в массиве
def count_elements(array):
    if not array:
        return 0
    return 1 + count_elements(array[1:])

print(count_elements([1, 4, 5 ,7 ,8]))


# Рекурсивный поиск максимального элемента в массиве
def max_number(array):
    if len(array) == 1:
        return array[0]
    return max(array[0], max_number(array[1:]))

print(max_number([1111, 17, 5 ,777 ,8]))