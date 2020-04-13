# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

var = input('Enter list of elements separate by space:\n').split(' ')

# i = 0
# while i < len(var[:-1]):
#     var[i], var[i + 1] = var[i + 1], var[i]
#     i += 2

for el in var[:-1:2]:
    var[var.index(el) + 1], var[var.index(el)] = var[var.index(el)], var[var.index(el) + 1]

print(var)
