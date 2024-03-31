class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
       print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} ест")

    def sing(self):
        print(f"{self.name} поёт - Чик-Чирик")

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Окрас: {self.color}")
        print(f"Голос: {self.voice}")

class Pijon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def sing(self):
        print(f"{self.name} поёт - Курлык-Курлык")

    def walk(self):
            print(f"{self.name} гуляет")

bird1 = Pijon("Гоша", "Курлык-Курлык", "Сизый", "Хлебные крошки")

bird2 = Bird("Кузя", "Кря-Кря", "Красный")

bird1.sing()
bird1.info()
bird1.walk()
bird2.sing()
