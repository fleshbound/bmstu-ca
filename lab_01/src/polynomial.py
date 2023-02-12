from table import *
from structures import EPS



def get_hermite_diff_table(diff_table, derivatives) -> list:
    """Получение таблицы разделенных разностей по конфигурации config_table
        с учетом направления интерполяции (полином Эрмита)"""

    length = len(diff_table[0])

    # len(config_table) === n + 1 ВСЕГДА
    for i in range(1, length, 1):
        new_y_list = []
        curr_y_list = diff_table[i]

        for j in range(0, length - i, 1):
            x_diff = diff_table[0][j] - diff_table[0][j + 1]

            if x_diff < EPS:
                new_y = derivatives[j // 2]
            else:
                new_y = (curr_y_list[j] - curr_y_list[j + 1]) / (diff_table[0][j] - diff_table[0][j + 1])

            new_y_list.append(new_y)

        diff_table.append(new_y_list)

    return diff_table


def get_newton_diff_table(config_table, is_backward) -> list:
    """Получение таблицы разделенных разностей по конфигурации config_table
        с учетом направления интерполяции (полином Ньютона)"""

    x_list = [point.x for point in config_table]
    y_list = [point.y for point in config_table]
    diff_table = []

    # Если обратная интерполяция, меняем столбцы
    if is_backward:
        diff_table = [y_list, x_list]
    else:
        diff_table = [x_list, y_list]

    # len(config_table) === n + 1 ВСЕГДА
    for i in range(1, len(config_table), 1):
        new_y_list = []
        curr_y_list = diff_table[i]

        for j in range(0, len(config_table) - i, 1):
            new_y = (curr_y_list[j] - curr_y_list[j + 1]) / (diff_table[0][j] - diff_table[0][j + 1])
            new_y_list.append(new_y)

        diff_table.append(new_y_list)

    return diff_table


def get_value_by_diff_table(diff_table, x) -> float:
    """Получение значения полинома при x по таблице разделенных разностей"""
    res_value = diff_table[1][0]
    curr_x = 1
    x_list = diff_table[0]

    for i in range(2, len(diff_table), 1):
        curr_y = diff_table[i][0]
        curr_x *= x - x_list[i - 2]
        res_value += curr_x * curr_y

    return res_value


def get_newton_polynomial_value(config_table, n, x) -> float:
    diff_table = get_newton_diff_table(config_table, False)
    # print_newton_diff_table(diff_table)
    res_value = get_value_by_diff_table(diff_table, x)

    return res_value
