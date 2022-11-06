# Применение list comprehension для улучшения кода

# Исходный код

print('Введите число')
n = int(input())
dic = {}
for i in range (1, n+1):
    dic[i] = (1 + 1/i)**i
print(dic)
total_sum = sum(dic.values())
print(total_sum)


# Применение list comprehension
print('Введите число')
n = int(input())
dic = {i: (1 + 1/i)**i for i in range (1, n+1)}
print(dic)
total_sum = sum(dic.values())
print(total_sum)