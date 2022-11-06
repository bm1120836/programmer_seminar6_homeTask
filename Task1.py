# Применение list comprehension для улучшения кода


# Задайте список из n чисел последовательности
# (1 + 1/n) в степени n и выведите на экран их сумму.
# Например, для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Первоначальный код
print('Введите число')
n = int(input())
dic = {}
for i in range (1, n+1):
    dic[i] = (1 + 1/i)**i
print(dic)
total_sum = sum(dic.values())
print(total_sum)

# Применение list comprehension
