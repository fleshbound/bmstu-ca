import polynomial
from table import *


def get_value_for_each_power(point_table, n_list, x) -> tuple:
    newton_value = hermite_value = []

    for n in n_list:
        config_table = get_config_table(point_table, n, x)
        diff_table = polynomial.get_newton_diff_table(config_table, False)

        if len(n_list) == 1:
            print("Таблица для полинома Ньютона")
            print_diff_table(diff_table)

        newton_value.append(polynomial.get_value_by_diff_table(diff_table, x))

        # hermite_value.append(hermite.get_hermite_polynomial_value(config_table, n, x))
        hermite_value.append(polynomial.get_newton_polynomial_value(config_table, n, x))

    return newton_value, hermite_value


def show_value_for_each_power(filename) -> None:
    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    x = float(input("Введите значение x: "))

    point_table = read_point_table(filename)
    print("\nИсходная таблица")
    print_point_table(point_table)

    newton_list, hermite_list = get_value_for_each_power(point_table, n_list, x)

    print_separator(3, 9)
    print("|{:^9s}|{:^9s}|{:^9s}|".format("n", "Ньютона", "Эрмита"))
    print_separator(3, 9)

    for i in range(len(n_list)):
        print("|{:^9d}|{:^9.3f}|{:^9.3f}|".format(n_list[i], newton_list[i], hermite_list[i]))

    print_separator(3, 9)
    print("")


def get_newton_backward_ip_root(point_table, n) -> float:
    config_table = get_config_table(point_table, n, 0)
    diff_table = polynomial.get_newton_diff_table(config_table, True)
    # newton.print_newton_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, 0)


def show_backward_interpolation_roots(filename) -> None:
    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    print("Значение x: 0")
    point_table = read_point_table(filename)

    print_separator(2, 9)
    print("|{:^9s}|{:^9s}|".format("n", "Ньютона"))
    print_separator(2, 9)

    for n in n_list:
        root = get_newton_backward_ip_root(point_table, n)
        print("|{:^9d}|{:^9.3f}|".format(n, root))
        print_separator(2, 9)


def find_system_roots(filename1, filename2) -> None:
   pass
