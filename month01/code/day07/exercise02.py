"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""
# for i in range(4):
#     for j in range(6):
#         if j % 2 == 0:
#             print("*", end="")
#         else:
#             print("#", end="")
#     print()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    *
    **
    ***
    ****
"""
# for i in range(4):
#     print("*"*(i+1))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    列表[3,80,45,5,7,1] (升序)
"""
# list01 = [3, 80, 45, 5, 7, 1]
# for i in range(len(list01)-1):
#     for j in range(i + 1, len(list01)):
#         if list01[i] < list01[j]:
#             list01[i], list01[j] = list01[j], list01[i]
# print(list01)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    判断列表中元素是否有相同
    所有元素两两比较，有相同则打印结果，没有发现则打印结果
"""
# leap = 0
# list01 = [3, 7, 89, 45, 45, 7, 80, 7, 1]
# for i in range(len(list01) - 1):
#     for j in range(i + 1, len(list01)):
#         if list01[i] == list01[j]:
#             leap = 1
#             print("list01[%d] = list01[%d] = %d" % (i, j, list01[i]))
# if leap == 0:
#     print("没有相同元素")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    list01 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
"""
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
# print(list01[1][2])
# for i in list01[2]:
#     print(i, end=" ")
# print()
# for i in range(4):
#     print(list01[i][0])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    矩阵转置，将二唯列表的列变成行
"""
# list01 = [
#      [11, 12, 13, 14, 15],
#      [21, 22, 23, 24, 25],
#      [31, 32, 33, 34, 35],
#      [41, 42, 43, 44, 45]
# ]
# result = []
# for i in range(len(list01[0])):
#     line = []
#     for j in range(len(list01)):
#         line.append(list01[j][i])
#     result.append(line)
# for i in result:
#     print(i)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    练习:列表的全排列
"""

# list_new = [i + j for i in ["香蕉", "苹果", "哈密瓜"] for j in ["可乐", "牛奶"]]
# print(list_new)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数
"""
# def star(x1, x2):
#
#     for i in range(x1):
#         for j in range(x2):
#             print("* ", end="")
#         print()
#
# star(6, 6)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    定义函数打印列表
"""

# def print_list(x_list):
#     """
#         打印二维列表
#     :param x_list: 目标列表
#     :return:
#     """
#     for i in x_list:
#         for j in i:
#             print(j, end=" ")
#         print()
#
#
# print_list([[1, 2, 3, 44],
#             [4, 5, 5, 5, 65, 6, 87],
#             [7, 5]])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    方阵转置算法
"""
# list01 = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# for i in range(len(list01)):
#     for j in range(i + 1, len(list01)):
#         print(i, j)
#         list01[i][j], list01[j][i] = list01[j][i], list01[i][j]
#
# for item in list01:
#     print(item)


# import time
#
# while True:
#     print(time.strftime("%H:%M:%S",time.localtime(time.time())))
#     time.sleep(1)
