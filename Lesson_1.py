# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f"\"{name}\"")  # Press ⌘F8 to toggle the breakpoint.

    # Task 1
    print("**** Task 1 ****")

    lv_birth_date = 2022 - int((input("Enter your age:")))  # можно использовать datetime и текущий год.
    print(f"Your birth year is: ", lv_birth_date)

    if (lv_birth_date % 4 == 0) and (lv_birth_date % 100 != 0):
        lv_leap_year = True
    else:
        lv_leap_year = False

    print(f"Birth year is leap year:", str(lv_leap_year))

    lv_i = 0
    while True:
        lv_birth_date += 1
        lv_i += 1
        if (lv_birth_date % 4 == 0) and (lv_birth_date % 100 != 0):
            print(f"Next leap year after your birth year is: {lv_birth_date}. iteration {lv_i}")
            break

    # Задача номер 2
    print("\n\n **** Task_2 ****  Seconds converter")

    while True:
        lv_sec = int(input("Enter seconds:"))
        if lv_sec >= 86400:
            print("Please, enter less than 86400 seconds")
        else:
            break

    print(f'{lv_sec // 3600:02d}:{lv_sec % 3600 // 60:02d}:{lv_sec % 3600 % 60:02d}')

    # Задача номер 3
    print("\n\n **** Task_3 ****  n+nn+nnn = ? ")
    lv_value = input("Enter n: ")

    print(f"n+n+nnn={int(lv_value) + int(lv_value + lv_value) + int(lv_value + lv_value + lv_value)}")

    # Задача номер 4
    print("\n\n **** Task_4 ****  max digit in input ")

    lv_value = input("Enter digit:")

    lv_max = 0
    for lv_literal in lv_value:
        if int(lv_literal) > lv_max:
            lv_max = int(lv_literal)

    print(f"Max digit is: {lv_max}")

    # Задача номер 5
    print("\n\n **** Task_5 ****  Revenues ")

    lv_revenue = float(input("Enter your revenue: "))
    lv_costs = float(input("Enter your costs: "))

# !!! Как тут лучше сделать? Вынести вычисления в переменные и потом составить разные строки или как уже сделал?
    if lv_revenue > lv_costs:
        lv_profit = f"You have profit: {lv_revenue - lv_costs}"
        lv_profitability = f"Your profitability is : {(lv_revenue - lv_costs) / lv_revenue}"
        lv_profitability_rate = f"Your profitability rate is : {(1 - (lv_revenue - lv_costs) / lv_revenue)}"

    else:
        lv_profit = f"You have loses: {lv_revenue - lv_costs}"
        lv_profitability = f"Your profitability is poor"
        lv_profitability_rate = "Same"

    print(lv_profit)
    print(lv_profitability)
    print(lv_profitability_rate)

    lv_staff = int(input("Enter your staff count:"))
    print(f"Your profit per employee is: {(lv_revenue - lv_costs) / lv_staff:0.3f}")

    # Задача номер 6
    print("\n\n **** Task_6 **** Sportsman ")

    lv_start_distance = float(input("Enter starting distance (a): "))
    lv_end_distance = float(input("Enter planning distance (b): "))

    print("\n--- Result ---")
    lv_cur_day = 0

    while True:
        lv_cur_day += 1

        # Результат бегуна на текущий день.
        print(f"{lv_cur_day} day: {lv_start_distance:0.3f}")

        # Изменение результата
        lv_start_distance = 1.1 * lv_start_distance
        if lv_start_distance >= lv_end_distance:
            print(f"Solution: sportsman got his planned distance on {lv_cur_day} day.")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Lesson_1')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
