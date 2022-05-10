# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod, abstractproperty
import datetime as dt


class NoInvExist(Exception):
    def __init__(self):
        print("No such inv number in warehouse!")


class InvExist(Exception):
    def __init__(self) -> str:
        print("Already added as a new item to WH!")


class Office_equipment(ABC):

    @property
    @abstractmethod
    def whois(self):
        pass

    @property
    @abstractmethod
    def label(self):
        """Марка техники"""
        pass

    @label.setter
    @abstractproperty
    def label(self, iv_label):
        pass

    @property
    @abstractmethod
    def cost(self, iv_cost):
        """Стоимость техники"""
        pass

    @cost.setter
    @abstractproperty
    def cost(self, iv_cost):
        pass

    @property
    @abstractmethod
    def inventory_code(self):
        """Инвентарный номер"""
        pass

    @inventory_code.setter
    @abstractproperty
    def inventory_code(self, iv_inventory):
        pass

    @abstractmethod
    def equip_func(self):
        """Функция, выполняющая работу техники"""
        pass


class Printer(Office_equipment):
    def __init__(self, iv_label, iv_cost, iv_inventory):
        self.__label = iv_label
        self.__cost = iv_cost
        self.__inventory = iv_inventory
        self.__type = "Printer"

    @property
    def whois(self):
        return self.__type

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, iv_label):
        self.__label = iv_label

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, iv_cost):
        self.__cost = iv_cost

    @property
    def inventory_code(self):
        return self.__inventory

    @inventory_code.setter
    def inventory_code(self, iv_inv: str):
        if iv_inv[0:2] != "PR":
            print("Incorrect inventory number (should start with \"PR\")")
            return
        self.__inventory = iv_inv

    def equip_func(self):
        self.__do_printing(self)

    def __do_printing(self):
        print("A4 is printed succesfully")


class Scanner(Office_equipment):
    def __init__(self, iv_label, iv_cost, iv_inventory):
        self.__label = iv_label
        self.__cost = iv_cost
        self.__inventory = iv_inventory
        self.__type = "Scanner"

    @property
    def whois(self):
        return self.__type

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, iv_label):
        self.__label = iv_label

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, iv_cost):
        self.__cost = iv_cost

    @property
    def inventory_code(self):
        return self.__inventory

    @inventory_code.setter
    def inventory_code(self, iv_inv: str):
        if iv_inv[0:2] != "SC":
            print("Incorrect inventory number (should start with \"SC\")")
            return
        self.__inventory = iv_inv

    def equip_func(self):
        self.__do_scanning(self)

    def __do_scanning(self):
        print("Scan-copy sent to your mail")


class Xerox(Office_equipment):
    def __init__(self, iv_label, iv_cost, iv_inventory):
        self.__label = iv_label
        self.__cost = iv_cost
        self.__inventory = iv_inventory
        self.__type = "Xerox"

    @property
    def whois(self):
        return self.__type

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, iv_label):
        self.__label = iv_label

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, iv_cost):
        self.__cost = iv_cost

    @property
    def inventory_code(self):
        return self.__inventory

    @inventory_code.setter
    def inventory_code(self, iv_inv: str):
        if iv_inv[0:2] != "XE":
            print("Incorrect inventory number (should start with \"XE\")")
            return
        self.__inventory = iv_inv

    def equip_func(self):
        self.__do_scanning_and_printing(self)

    def __do_scanning_and_printing(self):
        print("Scan-copy sent to your mail, some pages we printed.")


class WarehouseLocation:
    def __init__(self, iv_department, iv_move_date: dt.date):
        self.__current_department = iv_department
        self.__date_moved = iv_move_date

    @property
    def current_department(self):
        return self.__current_department

    @property
    def current_date(self):
        return self.__date_moved.__str__()


class Warehouse:
    def __init__(self):
        self.__devices = {}
        self.__movement_hstry = {}

    def add_equipment(self, equipment: Office_equipment):
        if self.__devices.get(equipment.inventory_code) != None:
            raise InvExist()

        self.__devices[equipment.inventory_code] = [equipment.whois, equipment,
                                                    whloc := WarehouseLocation("Warehouse13", dt.date.today())]
        self.__movement_hstry[equipment.inventory_code] = [whloc]

    def move_to_department(self, iv_inv_num, iv_new_department):
        try:
            new_wh_loc = WarehouseLocation(iv_new_department, dt.date.today())
            self.__devices[iv_inv_num][2] = new_wh_loc
            self.__movement_hstry[iv_inv_num].append(new_wh_loc)
        except KeyError as exc:
            raise NoInvExist()
        else:
            print(f"Device with inv {iv_inv_num} moved to {iv_new_department} sucessfully")

    def total_devices(self):
        return len(self.__devices)

    def show_current_move_history(self):
        for el in self.__movement_hstry:
            print(f"inv num {el} history records:")
            records = map(lambda x: "Located at " + x.current_department + " on date " + x.current_date,
                          self.__movement_hstry[el])
            for record in records:
                print(f"\t {record}")


# ______________________________________________________________________________________________________________________
if __name__ == "__main__":
    new_printer = Printer("Phaser", "20000", "PR0001")
    new_printer.label = "Phaser1232"

    print(new_printer.whois)
    print(new_printer.label)

    new_xerox = Xerox("Xer012", "25000", "XE0001")

    print(new_xerox.whois)
    print(new_xerox.label)

    wh = Warehouse()
    wh.add_equipment(new_printer)
    wh.move_to_department("PR0001", "Sales")

    wh.add_equipment(new_xerox)
    wh.move_to_department("XE0001", "Marketing")

    wh.show_current_move_history()
