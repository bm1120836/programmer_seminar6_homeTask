# Применение enumerate

# Исходный код. Код перемешивания списка

#import random
#print('Введите число')
#n = int(input())
#lst = []
#for i in range(n):
#   num = random.randint(1, 100)
#   lst.append(num)
#print('Основной список')
#print(lst)
# применяю функцию shuffle для перемешивания списка
#random.shuffle(lst)
#print('Перемешанный список')
#print(lst)

# Применение enumerate
import random
print('Введите число')
n = int(input())
lst = []
for i in range(n):
    num = random.randint(1, 100)
    lst.append(num)
enumLst = enumerate(lst, 1)
print('Основной список')
print(list(enumLst))
# применяю функцию shuffle для перемешивания списка
random.shuffle(lst)
enumLst = enumerate(lst, 1)
print('Перемешанный список')
print(list(enumLst))

