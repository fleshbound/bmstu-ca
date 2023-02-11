import table


def get_newton_diff_table(config_table) -> list:
    x_list = [point.x for point in config_table]
    y_list = [point.y for point in config_table]

    diff_table = [x_list, y_list]

    # len(config_table) === n - 2 ВСЕГДА
    for i in range(1, len(config_table), 1):
        new_y_list = []
        curr_y_list = diff_table[i]

        for j in range(0, len(config_table) - i, 1):
            new_y = (curr_y_list[j] - curr_y_list[j + 1]) / (x_list[j] - x_list[j + 1])
            new_y_list.append(new_y)

        diff_table.append(new_y_list)

    return diff_table


def print_newton_diff_table(diff_table) -> None:
    length = len(diff_table)

    print("╔" + "═" * 8 + ("╦" + "═" * 8) * (length - 1) + "╗")
    print("║ {:^6s} ║ {:^6s}".format("X", "Y"), end=' ')

    for k in range(2, length):
        print("║ {:^6s}".format("Y" + "\'" * (k - 1)), end=' ')
    print("║")
    print("╠" + "═" * 8 + ("╬" + "═" * 8) * (length - 1) + "╣")

    for i in range(length - 1):
        for j in range(length):
            if j >= length - i:
                print("║ {:^6s}".format(" "), end=' ')
            else:
                print("║ {:^6.3f}".format(diff_table[j][i]), end=' ')
        print("║")

    print("╚" + "═" * 8 + ("╩" + "═" * 8) * (length - 1) + "╝\n")


def get_newton_value_by_diff_table(diff_table, x) -> float:
    res_value = diff_table[1][0]
    curr_x = 0
    x_list = diff_table[0]

    for i in range(2, len(diff_table), 1):
        curr_y = diff_table[i][0]
        curr_x *= x - x_list[i - 2]
        res_value += curr_x * curr_y

    return res_value


def get_newton_polynomial_value(point_table, n, x) -> tuple:
    config_table = table.get_config_table(point_table, x, n)
    diff_table = get_newton_diff_table(config_table)
    res_value = get_newton_value_by_diff_table(diff_table, x)

    return diff_table, res_value
