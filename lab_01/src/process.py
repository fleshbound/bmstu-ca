import newton
import table


def get_newton_value_for_each_power(point_table, n_list, x) -> list:
    newton_value = []

    for n in n_list:
        res = newton.get_newton_polynomial_value(point_table, n, x)
        newton_value.append(res[1])

    return newton_value


def show_value_for_each_power(filename):
    n_list = list(map(int, input("Введите значения n: ").split(" ")))
    x = float(input("Введите значение x: "))
    point_table = table.read_point_table(filename)
    newton_values = get_newton_value_for_each_power(point_table, n_list, x)

    for y in newton_values:
        print("{:.3}".format(y))
