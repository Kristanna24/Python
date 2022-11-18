lesson_06.py
# ------------------------------------1------------------------------------
import time
import turtle
class TrafficLight(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.penup()

    def red(self):
        self.setposition(0, 40)
        self.color('red')
        self.penup()

    def yellow(self):
        self.setposition(0, 0)
        self.color('yellow')
        self.penup()

    def green(self):
        self.setposition(0, -40)
        self.color('green')
        self.penup()

t = TrafficLight()
t.red()
time.sleep(7)
t.yellow()
time.sleep(2)
t.green()
time.sleep(4)

# --------------------------другой вариант-----------------------------
from time import sleep

class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1
						
t = TrafficLight()
t.running()

# ------------------------------------2------------------------------------
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна, необходимо: {round(mass)} т.')
r = Road(5000, 20)
r.mass()

# ------------------------------------3------------------------------------
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Ivan', 'Ivanov', 'Director', '350000', '80000')
print(p.get_full_name(), p.get_total_income())

# ------------------------------------4------------------------------------
class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'Your speed is {self.speed}'

    def go(self):
        return f'The {self.name} go-go'

    def stop(self):
        return f'The {self.name} stop'

    def turn(self, side):
        return f'The {self.name} turned {side}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'You have exceeded the speed limit!'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'You have exceeded the speed limit!'
        else:
            return f'Speed of {self.name} is normal'

class PoliceCar(Car):
    pass

town = TownCar(70, 'blue', 'FordFocus', False)
print(town.go(), town.show_speed(), town.turn('left'), town.stop())

sport = SportCar(100, 'yellow', 'Ferrari', True)
print(sport.go(), sport.show_speed(), sport.turn('left'), town.turn('right'), sport.stop())

work = WorkCar(40, 'black', 'Scoda', True)
print(work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar(40, 'red', 'Volkswagen', False)
print(police.go(), police.show_speed(), police.turn('right'), police.stop())

# ------------------------------------5------------------------------------
import time

class Stationery:
    def __init__(self, title):
        self.title = title
        time.sleep(2)

    def draw(self):
        return f'Starting rendering'

class Pen(Stationery):
    def draw(self):
        return f'Starting rendering: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Starting rendering: {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Starting rendering: {self.title}'

pen = Pen('Pen')
print(pen.draw())
pencil = Pencil('Pencil')
print(pencil.draw())
handle = Handle('Handle')
print(handle.draw())

