'''Создать список из трех видов пиц'''
pizzas = ['пеперони', '3 сыра', 'мясная']

'''Вывести списком for все виды пиц'''
for pizza in pizzas:
    print(pizza)

'''Переработать цикл for чтобы для каждой пицы выводилось "Я люблю < название пиццы >'''
for pizza in pizzas:
    print(f"Я люблю {pizza}")

'''Вывести один раз после завершения цикла сообщение  < Любое >'''
print('Цикл завершился')




'''Использовать цикл for для вывода чисел от 1 до 20 включительно'''
for num in range(1, 21):
    print(num)
'''Создать список чисел от 1 до 10000. Вывести циклом for все числа.'''
nums = list(range(1,10000))
print(nums)
'''Суммировать все числа. Найти минимальное. Найти максимальное'''
print(sum(nums))
print(min(nums))
print(max(nums))
'''Вывести нечетные числа от 1 до 20'''
for i in range(1,30,2):
    print(i)
'''Вывести числа кратные 3'''
num_2 = []
for i in range(1,11):
    n = i ** 3
    num_2.append(n)
print(num_2)


print('-' * 20)

'''создать список из 6 элементов'''
spis = ['эл1', 'эл2', 'эл3', 'эл3', 'эл5', 'эл6']

'''Срезать первые 3 элемента'''
srez = spis[:3]

'''Перебрать их в цикле for (выводя вместе с сообщением)'''
for i in srez:
    print(f'Проверка {i}')