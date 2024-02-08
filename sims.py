import random


class Human:
    def __init__(self, name="nick", job=None, car=None, home=None):
        self.name = name
        self.job = job
        self.car = car
        self.home = home
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.thirst = 20

    def get_home(self):
        self.house = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("Food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def drink(self):
        if self.home.water <= 0:
            self.shopping("Water")
            self.thirst -= 20
            self.home.water -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness = self.job.gladness_less
        self.satiety -= 5
        self.thirst -= 2

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel = 100
        elif manage == "food":
            print("Bought food!")
            self.money -= 50
            self.home.food += 50
        elif manage == "water":
            print("Bought water!")
            self.money -= 5
            self.home.water += 5
        elif manage == "delicatecies":
            print("I`m Happy!")
            self.gladness += 10
            self.money -= 15
            self.satiety += 2

    def chill(self):
        if self.gladness < 20:
            print("Time to have some chill moment!")
            self.chill()
            self.gladness += 40
            self.thirst += 10
            self.satiety += 15
            self.mess += 25

    def clean_home(self):
        if self.mess > 0:
            manage = "cleaning"
        else:
            self.mess()
            return
        if manage == 'cleaning':
            print("I`ll clean this house!!")
            self.mess -= 30
            self.thirst += 10
            self.satiety += 10
            self.gladness += 5

    def to_repair(self):
        if self.strength < 10:
            print("I should repair my car!")
            self.to_repair()
            self.strength += 40
            self.money -= 100
            self.gladness += 20

    def days_indexes(self, day):
        d = f"Today the {day} of {self.name}`s indexes"
        print(f"{d:=^50}")
        human_i = f"{self.name}`s indexes"
        print(f"{human_i:=^50}")
        print(f"Gladness: {self.gladness}")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Thirst: {self.thirst}")
        house_i = f"{self.house} indexes"
        print(f"{house_i:=^50}")
        print(f"Mess: {self.house.mess}")
        print(f"Water: {self.house.water}")
        print(f"Food: {self.house.food}")
        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:=^50}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        elif self.satiety < 0:
            print("Dead...")
            return False
        elif self.money < 0:
            print("Bankrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settle in da Home")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get.job()
            print(f'I working at {self.job.job}, salary {self.job.salary}')
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 10:
            print("time to eat!")
            self.eat()
        elif self.gladness < 5:
            print('time chill')
            self.chill()
        elif self.money < 5:
            print("time to work")
            self.work()
        elif self.car.strength < 10:
            print('time to repair')
            self.to_repair()
        elif dice == 1:
            print("let`s chill")
            self.chill()
        elif dice == 2:
            print("Let`s working")
            self.work()
        elif dice == 3:
            print("time to clean")
            self.clean_home()
        elif dice == 4:
            manage = "delicatecies"
            self.shopping(manage)


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


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.glad = job_list[self.job]['gladness_less']


job_list = {"Python Developer": {"salary": 50, "gladness_less": 12},
            "C++ developer": {'salary': 70, 'glagness_less': 6},
            "Php developer": {'salary': 30, 'gladness_less': 4}}

brands_of_car = {"Mercedes": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Daewoo Lanos": {"fuel": 101, "strength": 300, "consumption": 20},
                 "Matiz": {"fuel": 120, "strength": 500, "consumption": 36},
                 "BMW M3 GTR": {"fuel": 100, "strength": 400, "consumption": 30}}

nick = Human("Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break
