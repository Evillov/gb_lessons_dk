# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Custom_date:
    def __init__(self, iv_date: str):
        self.__date = iv_date
        self.__date_list = [int(n) for n in iv_date.split(".")]

    @property
    def date_as_list(self):
        return self.__date_list

    @classmethod
    def get_num_from_data(cls, iv_date: str):
        new_obj = cls(iv_date)
        return new_obj

    @staticmethod
    def check_is_ok(iv_date: str) -> bool:
        iv_list = iv_date.split("-")
        if len(iv_list) > 3 or len(iv_list) < 3:
            return "incorrect date format"
        elif int(iv_list[0]) not in range(1, 32):
            return "incorrect day"
        elif int(iv_list[1]) not in range(1, 13):
            return "incorrect month"
        elif len(iv_list[2]) > 4 or len(iv_list[2]) < 4:
            return "incorrect year"
        return f"no problems"


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class Custom_exception(ZeroDivisionError):
    def __init__(self):
        print("Null deletion exception!!")


class Divider:
    @staticmethod
    def divide_two_float(a: float, b: float) -> float:
        if a == 0 or b == 0:  # также может быть вариант с обработкой исключения Zero exception и блок try/except
            raise Custom_exception
        return a / b


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class Custom_exception_onlydigit(Exception):
    def __init__(self, lv_input):
        self.exception_value = lv_input

    def get_exc_message(self):
        print(f"Entered value \"{self.exception_value}\" is not digit. Please enter correct one.")


class My_list(list):
    def append(self, lv_input: str) -> None:
        if not lv_input.isdigit():
            raise Custom_exception_onlydigit(lv_input)
        super().append(lv_input)


# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self, a, b=0):
        self.__a = int(a)
        self.__b = int(b)
        if b == 0:
            self.__j = False
        else:
            self.__j = True

    def __add__(self, other):
        return Complex(self.__a + other.__a, self.__b + other.__b)

    def __mul__(self, other):
        a = self.__a
        b = self.__b
        c = other.__a
        d = other.__b
        # (ac − bd) + (ad + bc) i
        im_part = a * d + b * c
        real_part = a * c - b * d

        return Complex(real_part, im_part)

    def __str__(self):
        return f"{self.__a} {str(self.__b) + 'j' if self.__j == True else ''}"


# ---------------------------------------------  MAIN  -------------------------------------------------------
if __name__ == "__main__":
    lv_task_n = int(input("Enter task num (1-7):\n"))
    if lv_task_n == 1:
        lv_check = Custom_date.check_is_ok(input("Enter your date (DD-MM-YYYY):\n"))
        print(f"Date has {lv_check}")

        print(instance_date.date_as_list)
        instance_date = Custom_date.get_num_from_data(input("Enter your date (DD.MM.YYYY):\n"))

    elif lv_task_n == 2:
        try:
            lv_result = Divider.divide_two_float(float(input("Enter num 1:")), float(input("Enter num 2:")))
        except Custom_exception as exc:
            print("no result")
            exit()
        print(lv_result)

    elif lv_task_n == 3:
        ls_list = My_list()
        while not (lv_input := input("Enter your digit (or \"stop\"):\n")) == "stop":
            try:
                ls_list.append(lv_input)
            except Custom_exception_onlydigit as exc:
                exc.get_exc_message()
        print(ls_list)

    elif lv_task_n == 7:
        a = Complex(1, 8)
        b = Complex(-3, 7)

        print(a + b)
        print(a * b)

        print(complex(1, 8) + complex(-3, 7))
        print(complex(1, 8) * complex(-3, 7))
