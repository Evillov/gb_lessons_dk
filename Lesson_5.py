import itertools as iter
from functools import reduce
import json


# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
def task_1_cr_file():
    print("Add new data:")
    with open(r"task_1_file.txt", "w+", encoding="utf-8") as f:
        while (lv_input := input()) != "":
            f.write(f'{lv_input}\n')


# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
def task_2_line_word_count():
    with open(r"task_1_file.txt", "r", encoding="utf-8") as f:
        lv_lines = 0
        lv_words = 0

        for line in f:
            lv_lines += 1
            lv_words = len(line.split())
            print(f"Words: {lv_words}")
        print(f"Lines {lv_lines}")

    # 3. Создать текстовый файл (не программно).
    # Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
    # Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
    # Выполнить подсчёт средней величины дохода сотрудников.
    # Пример файла:
    # Иванов 23543.12
    # Петров 13749.32


def task_3():
    with open(r"text_3.txt", "r", encoding="utf-8") as f:
        lv_dict = {name: float(salary) for name, salary in
                   (lv_splitter.split(" ") for lv_splitter in f.read().split("\n"))}
        print(lv_dict, type(lv_dict))

    lv_less_20000 = list(filter(lambda x: lv_dict[x] < 20000, lv_dict))
    print(lv_less_20000)

    # for name, salary in lv_dict.items():
    #     print(name, salary)

    # with open("text_3.txt", "r", encoding="utf-8") as f2:
    f2 = open(r"text_3.txt", "r", encoding="utf-8")
    lv_dict_2 = {n.split()[0]: float(n.split()[1]) for n in f2.__iter__()}
    print("V2", lv_dict_2)
    f2.close()

    lv_av = reduce(lambda x, y: x + y, lv_dict_2.values()) / len(lv_dict)
    # Среднее значение по доходности сотрудников.
    print(lv_av)


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
def task4():
    ld_translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

    with open(r"text_4.txt", "r", encoding="utf-8") as f:
        ld_from_file = {n.split("-")[0].strip(): n.split("-")[1].strip() for n in f}

    with open(r"text_4_n_txt", "w", encoding="utf-8") as f:
        for k, v in ld_from_file.items():
            print(f"{ld_translate.get(k)} - {v}", file=f)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
def task_5():
    lv_values = input("Enter digits:\n")

    with open(r"file_5.txt", "w", encoding="utf-8") as f:
        f.write(lv_values)

    lv_total = 0

    with open(r"file_5.txt", "r", encoding="utf-8") as f:
        lv_from_file = f.readline().strip()
        print(lv_from_file)
        for s in lv_from_file:
            lv_total += int(s)

    print(f"total {lv_total}")


# 6. Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб). Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
def task_6():
    ld_disciplines = {}
    ld_statistics = {}

    with open(r"text_6.txt", "r", encoding="utf-8") as f:
        # Физика: 120(л) 30(пр) -

        ld_disciplines = {n.split(":")[0].strip(): n.split(":")[1] for n in f}
    for k, v in ld_disciplines.items():
        lv_total = 0
        for dis in v.lstrip().split(" "):
            if dis.strip() == "-":
                continue

            lv_total += task_6_1_todigit(dis)

        ld_statistics.update({k: lv_total})
    print(f"new statistics {ld_statistics}")


def task_6_1_todigit(iv_str) -> int:
    list_digit = list(filter(lambda x: x.isdigit(), iv_str))
    rv_digit = 0
    try:
        rv_digit = int(reduce(lambda x, y: x + y, list_digit))
    except:
        pass
    return rv_digit


# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# [
# {firm:(OOO,1000,5000)},
# {firm2:(ZAO,5000,300)} ]
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
def task_7():
    ld_organization = dict()
    ld_final_org_list = dict()
    lv_org_list = list()
    lv_total_profit = float()
    lv_org_positive = int()
    lv_final_org_list = list()
    with open("text_7.txt", "r", encoding="utf-8") as f:
        for lv_line in f:
            lv_org_name = lv_line.split(" ")[0]
            # if (not lv_org_name.isascii()):
                # lv_org_name = lv_org_name.encode("")
            lv_org_form, lv_org_profit, lv_org_loss = \
                lv_line.split(" ")[1], int(lv_line.split(" ")[2]), int(lv_line.split(" ")[3])

            lv_profit = float(lv_org_profit - lv_org_loss)
            ld_organization.update(
                {lv_org_name: (lv_org_form,
                               lv_org_profit,
                               lv_org_loss,
                               lv_profit)
                 })
            # Если прибыль больше 0 то включаем в расчет средней прибыли.
            if (lv_profit > 0):
                lv_total_profit += lv_profit
                lv_org_positive += 1

    # lv_org_list.append(ld_organization)
    lv_total_profit = lv_total_profit / lv_org_positive
    print(ld_organization)
    # print(lv_org_list)

    # Собрали итоговый спискословарь
    for org, lv_chars in ld_organization.items():
        ld_final_org_list.update({org: lv_chars[3]})
    lv_final_org_list.append(ld_final_org_list)
    lv_final_org_list.append({"average_profit": lv_total_profit})

    print(lv_final_org_list)

    # TODO: сказкин форматируется в кривые символы. Что-то с кодировкой.
    with open("text_7_result.json", "w") as f:
        json.dump(lv_final_org_list, f, ensure_ascii=False) # три дня искал. пока 3 раз не пересмотрел запись вебинара..


# ****************************************** MAIN ******************************************#
if __name__ == "__main__":
    while (lv_task := int(input("Task?(1-7): \n"))) in range(1, 8):
        if (lv_task == 1):
            task_1_cr_file()
        elif (lv_task == 2):
            task_2_line_word_count()
        elif (lv_task == 3):
            task_3()
        elif (lv_task == 4):
            task4()
        elif (lv_task == 5):
            task_5()
        elif (lv_task == 6):
            task_6()
        elif (lv_task == 7):
            task_7()
