

def task_1(a=0.0, b=0.0) -> float:
    """
    1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
    """
    # try:
    #     lv_res = a/b
    # except Error :
    #     print("entered values cannot be divided")
    #     lv_res = None

    # return lv_res
    return a/b


def task2(name: str, lastname: str, year_birth: int, city: str, email: str, mobile: int) -> str:
    """ 
    2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

    Именованные параметры:
    name -- Имя
    lastname -- Фамилия
    year_birth -- Год рождения
    city -- Город проживания
    email -- Почта
    mobile --  Телефон

    """
    print(name, lastname, city, year_birth, mobile, email, sep=" ")
    return "Your data added to database"


def task3(a: float, b: float, c: float) -> float:
    """ 
    3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
    """
    lv_list = sorted(
        (a, b, c),
        reverse=True,
        key=lambda el: float(el)
    )

    print(lv_list)
    return sum(lv_list[0:2])


def task4(x: int, y: int):
    """ 
    4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
    Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

    Именованные параметры:
    Х -- целое положительное число.
    У -- Целое отрицательное число.

    """

    # Первый способ возведение в степень с помощью оператора **

    print(x ** (-y))

    # Второй способ реализация без оператора **, предусматривающая использование цикла
    res = 1
    for i in range(1, y+1):
        res *= x

    print(1/res)


def task5():
    """ 
    5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

    """
    lv_cumulative_sum = 0
    lv_iteration_sum = 0

    while True:
        lv_str = input("type your string with numbers:\n").replace(" ", "")
        print(lv_str)
        lv_flag_finish = False

        for el in lv_str:
            try:
                lv_iteration_sum += int(el)

            except ValueError as err:
                if el == "%":
                    lv_flag_finish = True  # Stop it.
                    break
                print(err)

        lv_cumulative_sum += lv_iteration_sum

        print(f"{lv_iteration_sum}({lv_cumulative_sum})")

        lv_iteration_sum = 0
        if lv_flag_finish:  # quit
            break


def task6(word: str) -> str:
    """ 
    6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
    """
    w = list(word)
    w[0] = w[0].upper()
    result = str()
    for el in w :
        result += el

    return result


def task7(sentence: str) -> str:
    """ 
    7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
    """
    r_result = str()
    for subs in sentence.split(' '):
        r_result += " " + task6(subs)
    
    return r_result.strip()


if(__name__ == "__main__"):

    while not ((lv_task_n := int(input("\nEnter task: "))) in range(1, 8)):
        pass

    if lv_task_n == 1:
        try:
            print("result:", res := task_1(
                float(input("\na:")), float(input("b:"))), end="\n\n")
        except ZeroDivisionError as err:
            print("Error: ", err)
        else:
            print("Go alternative!")
        finally:
            print("Go anyway!")

    elif lv_task_n == 2:

        lv_person_data_list = input(
            "Enter first name, last name, year birth, city, email, mobile:").split()

        print(task2(
            name=lv_person_data_list[0],
            lastname=lv_person_data_list[1],
            year_birth=int(lv_person_data_list[2]),
            city=lv_person_data_list[3],
            email=lv_person_data_list[4],
            mobile=lv_person_data_list[5]
        ))

    elif lv_task_n == 3:
        print(
            task3(
                int(input("a:")),
                int(input("b:")),
                int(input("c:"))
            )
        )

    elif lv_task_n == 4:
        try:
            task4(int(input()), int(input()))
        except TypeError as err:
            print("error: ", err)

    elif lv_task_n == 5:
        task5()

    elif lv_task_n == 6:
        print(task6(input("Tap the word:\n")))

    elif lv_task_n == 7:
        print(task7(input("Tap your sencence:\n")))
