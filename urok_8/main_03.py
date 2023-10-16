# Наследавание
# Работу над новым классом не обязательно начинать с нуля. Если класс которвй пишется представляет собой спец. версию ранее написанного класса, можно воспользоватся наследованием. Один класс наследующий от другого автоматически получает все атрибуты и методы первого класса.

# При написании нового класса на базе существующего класса часто приходится вызывать метод __init__() класса родителя. При этом происходит игициализация любых атрибутов, определенных в методе __init__() родителя, и эти атрибуты становятся доступны для класса-потомка


class Car():  # Класс родитель, должен предшествовать классу потомку.
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

    def update_odometr(self, km):
        '''Обновляет значение пробега машины. Проверка на скручивание пробега'''
        if km >= self.odometr_reading:
            self.odometr_reading = km
        else:
            print('Пробег Скручиваем!?')

    def increment_odometr(self, km):
        '''Увеличивает пробег с заданым приращением'''
        self.odometr_reading += km

    def oil(self):
        print('Машина исп. бензин')


class ElectricCar(Car):     # Класс потомок, В круглые скобки заключается имя класса родителя
    '''Електрокар '''
    def __init__(self, make, model, year):      # Метод __init__() получает инфу.,необходимую для создания экземпляра
        super().__init__(make, model, year)     # Функция super() - позволяет вызвать метод родительского класса. Приказывает вызвать метод __init__() класса Car, в результате чего класс ElectricCar получит доступ ко всем атрибутам класса-родителя

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())


# Определение атрибутов и методов класса-потомка

class ElectricCar(Car):   
    '''Електрокар '''
    def __init__(self, make, model, year): 
        '''Инициалдизирует атрибуты класса-родителя
        Затем ин. атрибуты, специфические для электромобиля
        '''     
        super().__init__(make, model, year) 
        self.battery_size = 80

    def describe_battery(self):
        '''Выводит информацию о мощьности аккумулятора'''
        print(f"Мощьность аккумулятора {self.battery_size}-kwh")

    def oil(self):
        '''У электрокаров нет бензобака'''
        print('Машмна не использует бензин')
    
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Любой метод родительского класса можно переопределить. Для этого в потомке определяется тот же метод с тем же названием что и в родителе. Питон игнорирует метод в родителе и берет метод потомка



# Экземпляры как атрибуты
# Наши классы могут разростись до огромных размеров и стобы не запутатся. Мы можем разбить один клас на более ментщие классы.

class Battery():        # Новвый класс
    '''Простая модель аккумулятора электромобиля'''
    def __init__(self, battery_size=75):
        '''Инициализирует атрибуты аккумулятора'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Выводит мощьность аккумулятора'''
        print(f"Мощьность аккумулятора {self.battery_size}-kwh")

class ElectricCar(Car):   
    '''Електрокар '''
    def __init__(self, make, model, year): 
        '''Инициалдизирует атрибуты класса-родителя
        Затем ин. атрибуты, специфические для электромобиля
        '''     
        super().__init__(make, model, year) 
        self.battery = Battery()    # Добавляется новый атрибут. Эта строка приказывает Питону создать новый экземпляр Battery и сохранить его в атрибутк self.battery

    def oil(self):
        '''У электрокаров нет бензобака'''
        print('Машмна не использует бензин')

# Чтобы вывести описание аккумулятора
my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())

res = my_tesla.battery.describe_battery()

print(res)
