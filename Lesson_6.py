import time
from random import choice


# Task_1 ********************
class TrafficLight:
    __pv_color = str()
    __pd_light_sec = {"Green": 7, "Yellow": 2, "Red": 10}

    def running(self, il_lights: list):
        for light in il_lights:
            print(light)
            time.sleep(self.__pd_light_sec[light])

        print("TrafficLight modulation is finished")


# Task 2 ********************
class EdRoad:
    """
    Класс Дорога.
    Имеет два protected аттрибута:
    Длина
    Ширина.

    Имеет метод для рассчета веса покрытия асфальта.
    На вход получает необходимый для расчета вес конкретной марки асфальта

    """
    _length = float()
    _width = float()

    def __init__(self, iv_length, iv_width):
        self._length = iv_length
        self._width = iv_width

    def weight_calc(self, iv_weight: float()):
        return (self._length * self._width * iv_weight * 5) / 1000


# Task3 ********************
class CustomWorker:
    cv_name = str()
    cv_surname = str()
    cv_position = str()
    _pr_income = dict()

    def __init__(self, iv_name: str, iv_surname: str, iv_wage: float, iv_bonus: float):
        CustomWorker._pr_income = {"wage": iv_wage, "bonus": iv_bonus}
        CustomWorker.cv_name = iv_name
        CustomWorker.cv_surname = iv_surname


class CustomPosition(CustomWorker):
    def get_full_name(self):
        return self.cv_name + self.cv_surname

    def get_total_income(self):
        return super()._pr_income.get("wage") + super()._pr_income.get("bonus")


# Task_4 ********************
class MyCar:
    def __init__(self, iv_speed: int, iv_name: str, iv_color: str, iv_is_police: bool = False):
        self.lc_speed = iv_speed
        self.lc_color = iv_color
        self.lc_name = iv_name
        self.lc_is_police = iv_is_police

    def go(self):
        print(f"\n{self.lc_name} Start moving!")

    def stop(self):
        print(f"{self.lc_name} Stop moving!")

    def turn(self, iv_direction: str):
        print(f"Car turned to {iv_direction}")

    def show_speed(self):
        print(f"Current speed is {self.lc_speed}")


class TownCar(MyCar):
    def show_speed(self):
        return print(self.lc_speed if self.lc_speed < 60 else f"{self.lc_speed} is a high speed (60 allowed)")


class WorkCar(MyCar):
    def show_speed(self):
        print(self.lc_speed if self.lc_speed < 40 else f"{self.lc_speed} is a high speed (40 allowed)")


class SportCar(MyCar):
    pass


class PoliceCar(MyCar):
    def __init__(self, lc_speed, lc_name, lc_color):
        super().__init__(self, lc_speed, lc_name, lc_color)
        self.lc_is_police = True

    def stop(self):
        print("Police car stopped!")


# Task_5 ***************************

class Stationery():
    def __init__(self, iv_title):
        self.lc_title = iv_title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.lc_title} drawing is blue!")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.lc_title} drawing is black!")


class Handle(Stationery):
    def draw(self):
        print(f"{self.lc_title} drawing is yellow!")


# ************************************** MAIN **********************************************
if __name__ == "__main__":
    lv_task = int(input("Task (1-5)?:"))

    if lv_task == 1:
        traffic_instance = TrafficLight()
        traffic_instance.running(il_lights=["Yellow", "Green", "Red", "Green"])
    elif lv_task == 2:
        road_instance = EdRoad(20.5, 5000)
        print(road_instance.weight_calc(25))
    elif lv_task == 3:
        my_position = CustomPosition("Alex", "Alexandrov", 3333.121, 499.20)
        print(f"My fullname is {my_position.get_full_name()} and my income is {my_position.get_total_income()}")
    elif lv_task == 4:
        lv_direction = ["Left", "Right", "forward", "backward"]

        my_towncar = TownCar(80, "Lada", "pink")
        my_sportcar = SportCar(200, "Maserati", "BlackMetallic")
        my_workcar = WorkCar(40, "Bobcat", "Orange")
        my_policecar = PoliceCar(80, "Ford", "White")

        my_towncar.go()
        my_towncar.show_speed()
        my_towncar.turn(choice(lv_direction))
        my_towncar.lc_name = "LadaGranta"
        my_towncar.stop()

        my_sportcar.go()
        my_sportcar.show_speed()
        my_sportcar.turn(choice(lv_direction))
        my_sportcar.stop()

        my_workcar.go()
        my_workcar.show_speed()
        my_workcar.turn(choice(lv_direction))
        my_workcar.stop()

        my_policecar.go()
        my_policecar.show_speed()
        my_policecar.turn(choice(lv_direction))
        my_policecar.stop()

    elif lv_task == 5:
        my_pen = Pen("Pen")
        my_pencil = Pencil("Pencil")
        my_handle = Handle("Handle")

        my_pen.draw()
        my_pencil.draw()
        my_handle.draw()