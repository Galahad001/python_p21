'''СТРОКИ'''
'''Программы собирают и обрабатываю некие данные. Строки - это тип данных
-Строка - это простая последовательность символов. Любая последовательность символов заключеная в кавычки - это строка'''

name = "иван иванов"
print(name.title())         # Метод title() преобразует первый символ каждого слова в верхний регистр
print(name.upper())         # Преобразует все символы в верхний регистр
print(name.lower())         # Преобразует все символы в нижний регистр
print(name.capitalize())    # Преобразует толко первый символ в вехний регистр


print()


'''f-строки'''
first_name = 'олег'
last_name = 'олегович'
full_name = f"{first_name} {last_name}"
msg = f"Привет {full_name.title()}"
print(full_name)
print(msg)