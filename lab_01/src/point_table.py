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
    print("╔" + "═" * 7 + ("╦" + "═" * 12) * 3 + "╗")
    print("║ {:^5s} ║ {:^10s} ║ {:^10s} ║ {:^10s} ║".format("№", "x", "y", "y\'"))
    print("╠" + "═" * 7 + ("╬" + "═" * 12) * 3 + "╣")

    for i in range(len(point_table)):
        print("║ {:^5d} ║ {:^10.3f} ║ {:^10.3f} ║ {:^10.3f} ║".format(i,
                                                                      point_table[i].x,
                                                                      point_table[i].y,
                                                                      point_table[i].dy))
    print("╚" + "═" * 7 + ("╩" + "═" * 12) * 3 + "╝\n")


def get_nearest_index(point_table, x) -> int:
    diff = abs(point_table[0].x - x)
    nearest_index = 0

    for i in range(len(point_table)):
        if abs(point_table[i].x - x) < diff:
            diff = abs(point_table[i].x - x)
            nearest_index = i

    return nearest_index


def get_config_table(point_table, index, n) -> list:
    low = high = index

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
