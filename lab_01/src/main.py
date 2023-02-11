import newton
import point_table


def print_menu() -> None:
    print("Доступные команды:")
    print("1. Получить таблицу значений y(x) при разл. n и фикс. x (Ньютон, Эрмит)")
    print("2. Найти корень табличной функции с помощью обратной интерполяции")
    print("3. Решить систему нелинейных уравнений")
    print("4. Показать меню")
    print("0. Выход")


def print_info() -> None:
    print("Программа предназначена для реализации алгоритма полиномиальной интерполяции табличных функций")
    print("Студент: Авдейкина В.П. (ИУ7-43Б)\n")


is_working = True
print_info()
print_menu()

while is_working:
    choice = int(input("Номер команды: "))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("")
        print_menu()
    elif choice == 0:
        print("Работа программы успешно завершена")
        is_working = False