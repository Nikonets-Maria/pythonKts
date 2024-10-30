# Задание 9: Виртуальный плоттер поддерживает пять команд: 
# Переместить каретку на некоторое расстояние в текущем 
# направлении. Повернуть на определенное количество градусов по
# часовой стрелке или против часовой стрелки. Опустить или 
# поднять каретку. Когда каретка опущена, плоттер при 
# перемещении рисует линию. Установить цвет линии (один из 
# черного, красного или зелёного). Установить начальную позицию 
# каретки.   Код в рабочем состоянии (можете запустить его) и 
# хорошо откомментирован.   Ваша задача разобраться в коде и 
# переписать его в объектно-ориентированном стиле. Вы должны 
# реализовать как минимум два класса: Plotter - основной класс 
# LogToConsole - класс, который реализует абстрактный класс 
# Logger, для логирования действий плоттера. LogToConsole должен 
# выводить информацию в консоль.   Код абстрактного класса 
# Logger: import abc class Logger(abc.ABC): @abc.abstractmethod 
# log(self, message: string) -> None: pass   Ваш код должен 
# отработать на следующем примере: def draw_triangle(plotter, 
# size): plotter.set_color('Green') 
# for _ in range(2): plotter.carriage_down() 
# plotter.move(size) plotter.carriage_up() 
# plotter.turn(120.0) plotter = Plotter(LogToConsole) 
# draw_triangle(plotter, 100.0)   
# Результат работы программы в консоли должен быть примерно 
# таким: Устанавливаем зелёный цвет линии. Опускаем каретку ...
# Чертим линию из (0, 0) в (100, 0) используя зелёный цвет. 
# Поднимаем каретку Поворачиваем на 120 градусов Опускаем 
# каретку ...Чертим линию из (100, 0) в (50, 87) используя 
# зелёный цвет. Поднимаем каретку Поворачиваем на 120 градусов 
# Опускаем каретку ...Чертим линию из (50, 87) в (0, 0) 
# используя зелёный цвет. Поднимаем каретку Поворачиваем на 
# 120 градусов 
# Задание Преобразуйте код в объектно-ориентированный

import abc
import math

class Logger(abc.ABC):
    @abc.abstractmethod
    def log(self, message: str) -> None:
        pass

class LogToConsole(Logger):
    def log(self, message: str) -> None:
        print(message)

class Plotter:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.x = 0.0
        self.y = 0.0
        self.angle = 0.0
        self.pen_down = False
        self.color = "Black"
        self.logger.log("Плоттер распознан.")


    def set_color(self, color: str) -> None:
        if color not in ["Black", "Red", "Green"]:
            self.logger.log(f"Ошибка: Неверный цвет '{color}'. Используется черный цвет.")
            return
        self.color = color
        self.logger.log(f"Устанавливаем {self.color} цвет линии.")

    def carriage_down(self) -> None:
        self.pen_down = True
        self.logger.log("Опускаем каретку.")

    def carriage_up(self) -> None:
        self.pen_down = False
        self.logger.log("Поднимаем каретку.")

    def turn(self, angle_degrees: float) -> None:
        self.angle += angle_degrees
        self.logger.log(f"Поворачиваем на {angle_degrees} градусов.")

    def move(self, distance: float) -> None:
        if not self.pen_down:
          self.logger.log(f"Перемещаем каретку на {distance} единиц без линии.")
          self.x += distance * math.cos(math.radians(self.angle))
          self.y += distance * math.sin(math.radians(self.angle))
          return

        new_x = self.x + distance * math.cos(math.radians(self.angle))
        new_y = self.y + distance * math.sin(math.radians(self.angle))
        self.logger.log(f"Чертим линию из ({self.x:.2f}, {self.y:.2f}) в ({new_x:.2f}, {new_y:.2f}) используя {self.color} цвет.")
        self.x = new_x
        self.y = new_y


    def set_position(self, x: float, y: float):
        self.x = x
        self.y = y
        self.logger.log(f"Устанавливаем начальную позицию каретки: ({self.x}, {self.y})")


def draw_triangle(plotter, size):
    plotter.set_color('Green')
    for _ in range(3):
        plotter.carriage_down()
        plotter.move(size)
        plotter.carriage_up()
        plotter.turn(120.0)

plotter = Plotter(LogToConsole())
draw_triangle(plotter, 100.0)

