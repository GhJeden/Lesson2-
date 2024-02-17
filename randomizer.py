from random import choice

class Randomizer:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __get_result(self):
        temp =["+", "-", "*"]
        oper = choice(temp)
        if oper == "+":
            return self.__a + self.__b
        if oper == "-":
            return self.__a - self.__b
        if oper == "*":
            return self.__a * self.__b

    def result(self):
        return self.__get_result()


r = Randomizer(12, 5)
print(r.result())