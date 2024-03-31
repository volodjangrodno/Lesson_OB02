class Car:
    def __init__(self, made, color, max_speed):
        self.public_made = made # публичное свойство
        self._protected_color = color # защищенное свойство
        self.__private_max_speed = 200 # приватное свойство

    def public_info(self):
        return (f"Это публичная информация. Производитель: {self.public_made}, цвет: {self._protected_color}")

    def _protected_info(self):
        return "Это защищённая информация"

    def __private_info(self):
        return "Это приватная информация"

class ElectricCar(Car):
    def __init__(self, made, color,  battery_size):
        super().__init__(made, color, 200)
        self.battery_size = battery_size

    def get_details(self):
        details = (f"self.public_made: {self.public_made}, self._protected_color: {self._protected_color}, "
                   f"Батарея: {self.battery_size} Кв/ч")
        return details
# создание экземпляра
tesla = ElectricCar("Tesla", "Black", 100)

# получение информации
print(tesla.public_made)
print(tesla.public_info())

# получение защищенной информации
print(tesla._protected_color)
print(tesla._protected_info())

# получение приватной информации
print(tesla._Car__private_max_speed)