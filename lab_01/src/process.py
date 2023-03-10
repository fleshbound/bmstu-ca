import polynomial
from table import *


def get_newton_value(point_table, n, x, verbose) -> float:
    config_table = get_config_table(point_table, n, x, False)
    diff_table = polynomial.init_newton_diff_table(config_table[0], config_table[1], False)
    polynomial.fill_newton_diff_table(diff_table)

    if verbose:
        print("\nТаблица разделенных разностей (полином Ньютона)")
        print_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, x)


def get_hermite_value(point_table, n, x, verbose) -> float:
    config_table = get_config_table(point_table, n, x, True)
    diff_table = polynomial.init_hermite_diff_table(config_table[0], config_table[1], n, False)
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

    x = float(input("Введите значение x: "))
    n_list = list(map(int, input("Введите значения n: ").split(" ")))

    newton_list, hermite_list = get_value_for_each_power(point_table, n_list, x)

    print_separator(3, 10)
    print("|{:^10s}|{:^10s}|{:^10s}|".format("n", "Ньютона", "Эрмита"))
    print_separator(3, 10)

    for i in range(len(n_list)):
        print("|{:^10d}|{:^10.3f}|{:^10.3f}|".format(n_list[i], newton_list[i], hermite_list[i]))

    print_separator(3, 10)
    print("")


def get_newton_backward_ip_root(point_table, n) -> float:
    point_table[0], point_table[1] = point_table[1], point_table[0]
    config_table = get_config_table(point_table, n, 0, False)
    diff_table = polynomial.init_newton_diff_table(config_table[1], config_table[0], True)
    polynomial.fill_newton_diff_table(diff_table)
    # print_diff_table(diff_table)

    return polynomial.get_value_by_diff_table(diff_table, 0)


def get_hermite_backward_ip_root(point_table, n) -> float:
    point_table[0], point_table[1] = point_table[1], point_table[0]
    config_table = get_config_table(point_table, n, 0, True)
    diff_table = polynomial.init_hermite_diff_table(config_table[0], config_table[1], n, True)
    polynomial.fill_hermite_diff_table(diff_table, list(map(lambda x: 1 / x, config_table[2])))

    return polynomial.get_value_by_diff_table(diff_table, 0)


def show_backward_interpolation_roots(filename) -> None:
    print("Значение x: 0")
    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    point_table = read_point_table(filename)

    print_separator(3, 10)
    print("|{:^10s}|{:^10s}|{:^10s}|".format("n", "Ньютона", "Эрмита"))
    print_separator(3, 10)

    for n in n_list:
        newton_root = get_newton_backward_ip_root(point_table, n)
        hermite_root = get_hermite_backward_ip_root(point_table, n)

        print("|{:^10d}|{:^10.3f}|{:^10.3f}|".format(n, newton_root, hermite_root))

    print_separator(3, 10)


def subtract_system_table(system_table) -> list:
    new_table = [[], [], []]

    for i in range(len(system_table)):
        new_table[0].append(system_table[i][0])
        new_table[1].append(system_table[i][1] - system_table[i][2])
        new_table[2].append(None)

    return new_table


def find_system_roots(filename1, filename2) -> None:
    point_table1, point_table2 = read_system_table(filename1), read_system_table(filename2)

    diff_table1 = polynomial.init_newton_diff_table(point_table1[0], point_table1[1], True)
    polynomial.fill_newton_diff_table(diff_table1)
    
    new_table = [[], [], []]
    
    for i in range(len(point_table2[0])):
        point_table2[2][i] = polynomial.get_value_by_diff_table(diff_table1, point_table2[0][i])
        
        new_table[0].append(point_table2[0][i])
        new_table[1].append(point_table2[1][i] - point_table2[2][i])
        new_table[2].append(None)
        
    print("Новая таблица")
    print_separator(3, 7)
    print("|{:^7s}|{:^7s}|{:^7s}|".format("№", "x", "y1-y2"))
    print_separator(3, 7)

    for i in range(len(new_table[0])):
        print("|{:^7d}|{:^7.3f}|{:^7.3f}|".format(i, new_table[0][i], new_table[1][i]))

    print_separator(3, 7)
    
    root = get_newton_backward_ip_root(new_table, 3)
    diff_table2 = polynomial.init_newton_diff_table(point_table2[0], point_table2[1], False)
    polynomial.fill_newton_diff_table(diff_table2)
    root_y = polynomial.get_value_by_diff_table(diff_table2, root)
    print("Решение системы: x= {:.3f}, y = {:.3f}".format(root, root_y))
