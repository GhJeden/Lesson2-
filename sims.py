import random


class Human:
    def __init__(self, name="Human", job=None, car=None):
        self.name = name
        self.job = job
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self):
        pass

    def is_alive(self):
        pass

    def live(self, day):
        pass


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.water = 0


brands_of_car = {"Mercedes": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Daewoo Lanos": {"fuel": 101, "strength": 300, "consumption": 20},
                 "Matiz": {"fuel": 120, "strength": 500, "consumption": 36},
                 "BMW M3 GTR": {"fuel": 100, "strength": 400, "consumption": 30}}
