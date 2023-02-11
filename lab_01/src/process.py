# filename = "../data/1.txt"
#
# print("Программа предназначена для реализации алгоритма полиномиальной интерполяции табличных функций")
# print("x - аргумент, для которого выполняется интерполяция (вещественный)")
# print("n - степень аппроксимирующих полиномов Ньютона и Эрмита")
#
# x = float(input("Введите значение x: "))
# n = int(input("Введите n: "))
#
# table = point_table.read_point_table(filename)
# #print("Main table:")
# #point_table.print_point_table(table)
#
# index = point_table.get_nearest_index(table, x)
# conf_table = point_table.get_config_table(table, index, n)
# print("Config table:")
# point_table.print_point_table(conf_table)
#
# diff_table = newton.get_newton_diff_table(conf_table)
# print("Divided differences")
# newton.print_newton_diff_table(diff_table)