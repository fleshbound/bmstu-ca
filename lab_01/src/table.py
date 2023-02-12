from structures import Point


def read_point_table(filename) -> list:
    point_table = []
    f = open(filename)

    for line in f.readlines():
        point_list = list(map(float, line.split(" ")))
        point_table.append(Point(point_list[0], point_list[1], point_list[2]))

    f.close()

    return point_table


def print_point_table(point_table) -> None:
    print_separator(4, 7)
    print("|{:^7s}|{:^7s}|{:^7s}|{:^7s}|".format("№", "x", "y", "y\'"))
    print_separator(4, 7)

    for i in range(len(point_table)):
        print("|{:^7d}|{:^7.3f}|{:^7.3f}|{:^7.3f}|".format(i, point_table[i].x,
                                                           point_table[i].y,
                                                           point_table[i].dy))
    print_separator(4, 7)
    print("")


def print_separator(length, step) -> None:
    print("+" + ("-" * step + "+") * length)


def get_nearest_index(point_table, x) -> int:
    diff = abs(point_table[0].x - x)
    nearest_index = 0

    for i in range(len(point_table)):
        if abs(point_table[i].x - x) < diff:
            diff = abs(point_table[i].x - x)
            nearest_index = i

    return nearest_index


def get_config_table(point_table, n, x) -> list:
    low = high = get_nearest_index(point_table, x)

    for i in range(0, n, 1):
        if i % 2 != 0:
            if low == 0:
                high += 1
            else:
                low -= 1
        else:
            if high == len(point_table) - 1:
                low -= 1
            else:
                high += 1

    return point_table[low:high + 1]


def print_diff_table(diff_table) -> None:
    length = len(diff_table)

    print_separator(length, 7)
    print("|{:^7s}|{:^7s}".format("x", "y"), end='')

    for i in range(2, length):
        print("|{:^7s}".format("y" + "\'" * (i - 1)), end='')

    print("|")
    print_separator(length, 7)

    for i in range(length - 1):
        for j in range(length):
            if j >= length - i:
                print("|{:^7s}".format(" "), end='')
            else:
                print("|{:^7.3f}".format(diff_table[j][i]), end='')

        print("|")

    print_separator(length, 7)
    print("")
