import time
from random import randint
import os

def log(func):

    def wrapper(*args, **kwargs):
        logFile = open("machine.log", "a")
        start_time = time.time() * 1000
        ret = func(*args, **kwargs)
        end_time = (time.time() * 1000) - start_time
        if end_time < 1000.0:
            end_time = "{:.3f} ms".format(end_time)
        else:
            end_time = "{:.3f} s ".format(end_time / 1000.0)
        logFile.write("({})Running: {:<19}[ exec-time = {} ]\n".format(os.environ['USER'], func.__name__, end_time))
        logFile.close()
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
