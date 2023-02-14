import process


def print_menu() -> None:
    print("Доступные команды:")
    print("1. Получить таблицу значений y(x) при разл. n и фикс. x (Ньютон, Эрмит)")
    print("2. Найти корень табличной функции с помощью обратной интерполяции")
    print("3. Решить систему нелинейных уравнений")
    print("4. Показать меню")
    print("0. Выход")


def print_info() -> None:
    print("Программа предназначена для реализации алгоритма полиномиальной\nинтерполяции табличных функций")
    print("Студент: Авдейкина В.П. (ИУ7-43Б)\n")


is_working = True
print_info()
print_menu()

while is_working:
    choice = int(input("Номер команды (4 - меню): "))

    if choice == 1:
        process.show_value_for_each_power("../data/1.txt")
    elif choice == 2:
        process.show_backward_interpolation_roots("../data/1.txt")
    elif choice == 3:
        process.find_system_roots("../data/3_1.txt", "../data/3_2.txt")
    elif choice == 4:
        print("")
        print_menu()
    elif choice == 0:
        print("Работа программы успешно завершена")
        is_working = False
