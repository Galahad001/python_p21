# Работа с классами и экземплярами

class Car():
    '''Модель автомобиля'''
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''Возв. аккуратно отформатированое описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('ауди', 'q7', 2021)
print(my_new_car.get_descriptive_name())



# Назначение атрибута по умолчанию

class Car():
    '''Модель автомобиля'''
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0 #

    def get_descriptive_name(self):
        '''Возв. аккуратно отформатированое описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometr(self):
        '''Выводит пробег машины'''
        print(f"Пробег машины {self.odometr_reading} км")

    # Вариант 2
    def update_odometr(self, km):
        '''Обновляет значение пробега машины. Проверка на скручивание пробега'''
        if km >= self.odometr_reading:
            self.odometr_reading = km
        else:
            print('Пробег Скручиваем!?')

    # Вариант 3
    def increment_odometr(self, km):
        '''Увеличивает пробег с заданым приращением'''
        self.odometr_reading += km


my_new_car = Car('ауди', 'q7', 2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometr()


# Изменение значений атрибутов

    # 1 Вариант - прямое изменение
my_new_car.odometr_reading  = 100
my_new_car.read_odometr()

    # 2 Вариант - изменение атрибута с использованием метода

my_new_car.update_odometr(200)
my_new_car.read_odometr()

    # 3 Вариант - изменение атрибута с приращением
my_used_car = Car('хендай', 'палисад', 2022)
print(my_used_car.get_descriptive_name())\

my_used_car.update_odometr(20_000)
my_used_car.read_odometr()

my_used_car.increment_odometr(1000)
my_used_car.read_odometr()