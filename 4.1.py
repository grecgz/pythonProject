#  4.1 Выбор из двух /  шаг 8
#  Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
#  Формат входных данных
#  На вход программе подаются три числа, каждое на отдельной строке.
#  Формат выходных данных
#  Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи.
#  Sample Input 1:
#  1
#  2
#  3
#  Sample Output 1:
#  YES
#  Sample Input 2:
#  1
#  2
#  4
#  Sample Output 2:
#  NO
#                       4.1.8
# a, b, c = int(input()), int(input()), int(input())
# an = b
# if an == (a + c) / 2:
#     print('YES')
# else:
#     print('NO')
#                       4.1.9
# x, y = int(input()), int(input())
# if x > y:
#     print(y)
# else:
#     print(x)
#                       4.1.10
x, y, z, w = int(input()), int(input()), int(input()), int(input())
if x < y:
    x = y
if z < w:
    z = w
if x < z:
    x = z
else:
    print(x)
    