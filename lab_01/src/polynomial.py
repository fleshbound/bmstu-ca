def init_hermite_diff_table(x_list, y_list, n, is_backward) -> list:
    """Инициализация таблицы разделенных разностей с учетом направления интерполяции (полином Эрмита)"""

    diff_table = [[xi for x in x_list for xi in [x, x]],
                  [yi for y in y_list for yi in [y, y]]]

    # Если обратная интерполяция, меняем столбцы
    if is_backward:
        diff_table = [[yi for y in y_list for yi in [y, y]],
                      [xi for x in x_list for xi in [x, x]]]

    if (n + 1) % 2 != 0:
        diff_table[0].pop()
        diff_table[1].pop()

    return diff_table


def fill_hermite_diff_table(diff_table, derivatives) -> None:
    """Заполнение таблицы разделенных разностей по конфигурации config_table (полином Эрмита)"""

    length = len(diff_table[0])

    # length === n * 2 ВСЕГДА
    for i in range(1, length, 1):
        new_y_list = []
        curr_y_list = diff_table[i]

        for j in range(0, length - i, 1):
            x_diff = diff_table[0][j] - diff_table[0][j + i]

            if x_diff == 0 and i == 1:
                new_y = derivatives[j // 2]
            else:
                new_y = (curr_y_list[j] - curr_y_list[j + 1]) / x_diff

            new_y_list.append(new_y)

        diff_table.append(new_y_list)

    return diff_table


def init_newton_diff_table(x_list, y_list, is_backward) -> list:
    """Инициализация таблицы разделенных разностей с учетом направления интерполяции (полином Ньютона)"""

    diff_table = [x_list, y_list]

    # Если обратная интерполяция, меняем столбцы
    if is_backward:
        diff_table = [y_list, x_list]

    return diff_table


def fill_newton_diff_table(diff_table) -> None:
    """Получение таблицы разделенных разностей по конфигурации config_table (полином Ньютона)"""

    length = len(diff_table[0])

    # length === n + 1 ВСЕГДА
    for i in range(1, length, 1):
        new_y_list = []
        curr_y_list = diff_table[i]

        for j in range(0, length - i, 1):
            new_y = (curr_y_list[j] - curr_y_list[j + 1]) / (diff_table[0][j] - diff_table[0][j + i])
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
