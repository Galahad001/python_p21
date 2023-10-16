class Car():
    '''Модель автомобиля'''
    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0 

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


class Battery():  
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


my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

