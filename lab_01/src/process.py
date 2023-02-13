import polynomial
from table import *


def get_newton_value(point_table, n, x, verbose) -> float:
    config_table = get_config_table(point_table, n, x)
    diff_table = polynomial.init_newton_diff_table(config_table[0], config_table[1], False)
    polynomial.fill_newton_diff_table(diff_table)

    if verbose:
        print("\nТаблица разделенных разностей (полином Ньютона)")
        print_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, x)


def get_hermite_value(point_table, n, x, verbose) -> float:
    config_table = get_config_table(point_table, n, x)
    diff_table = polynomial.init_hermite_diff_table(config_table[0], config_table[1], False)
    polynomial.fill_hermite_diff_table(diff_table, config_table[2])

    if verbose:
        print("\nТаблица разделенных разностей (полином Эрмита)")
        print_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, x)


def get_value_for_each_power(point_table, n_list, x) -> tuple:
    newton_value = []
    hermite_value = []
    verbose = True if len(n_list) == 1 else False

    for n in n_list:
        newton_value.append(get_newton_value(point_table, n, x, verbose))
        hermite_value.append(get_hermite_value(point_table, n, x, verbose))

    return newton_value, hermite_value


def show_value_for_each_power(filename) -> None:
    point_table = read_point_table(filename)
    print("\nИсходная таблица")
    print_point_table(point_table)

    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    x = float(input("Введите значение x: "))

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
    diff_table = polynomial.init_newton_diff_table(config_table[0], config_table[1], True)
    polynomial.fill_newton_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, 0)


def get_hermite_backward_ip_root(point_table, n) -> float:
    config_table = get_config_table(point_table, n, 0)
    diff_table = polynomial.init_hermite_diff_table(config_table[0], config_table[1], True)
    polynomial.fill_hermite_diff_table(diff_table, list(map(lambda x: 1 / x, config_table[2])))

    return polynomial.get_value_by_diff_table(diff_table, 0)


def show_backward_interpolation_roots(filename) -> None:
    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    print("Значение x: 0")
    point_table = read_point_table(filename)

    print_separator(3, 9)
    print("|{:^9s}|{:^9s}|{:^9s}|".format("n", "Ньютона", "Эрмита"))
    print_separator(3, 9)

    for n in n_list:
        newton_root = get_newton_backward_ip_root(point_table, n)
        hermite_root = get_hermite_backward_ip_root(point_table, n)

        print("|{:^9d}|{:^9.3f}|{:^9.3f}|".format(n, newton_root, hermite_root))
        print_separator(3, 9)


def find_system_roots(filename1, filename2) -> None:
   pass
