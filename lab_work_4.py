from dataclasses import dataclass
from abc import ABC


@dataclass
class Engine(ABC):
    power: int
    company: str

    def __str__(self):
        return f"Engine power {self.power} and produced by {self.company}"


@dataclass
class Person(ABC):
    age: int
    fullName: str

    def __str__(self):
        return f'{self.fullName} is {self.age} years old'


@dataclass
class Driver(Person):
    experience: int

    def __str__(self):
        return f'Driver {self.fullName} had {self.experience} years of driving experience'


@dataclass
class Car(ABC):
    carClass: str
    engine: Engine
    driver: Driver
    marka: str

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnRight(self):
        print('Поворот направо')

    def turnLeft(self):
        print('Поворот налево')

    def __str__(self):
        return f'car class is {self.carClass}, marka is {self.marka}, driver of this ' \
               f'car is {self.driver}, and engine is {self.engine}'

@dataclass()
class Lorry(Car):
    carrying: int

    def __str__(self):
        return f'Driver: {self.driver}\n' \
               f'carClass: {self.carClass}\n' \
               f'engine: {self.engine}\n' \
               f'marka: {self.marka}\n' \
               f'carrying: {self.carrying}' \


@dataclass()
class SportCar(Car):
    speed: float

    def __str__(self):
        return f'Driver: {self.driver}\n' \
               f'carClass: {self.carClass}\n' \
               f'engine: {self.engine}\n' \
               f'marka: {self.marka}\n' \
               f'speed: max is {self.speed}'


engine1 = Engine(power=250, company='Lamborghini')
driver1 = Driver(fullName="Almas ", age=26, experience=3)
lamborghini = SportCar(carClass='Sport', engine=engine1, driver=driver1,
                       marka='Lambarghini', speed=350.4)
print(lamborghini)

engine2 = Engine(power=200, company='Mercedes')
driver2 = Driver(fullName="Miras ", age=35, experience=15)
Mercedes_Truck = Lorry(carClass='Lorry', engine=engine2, driver=driver2,
                       marka='Mercedes', carrying=5500)
print(Mercedes_Truck)