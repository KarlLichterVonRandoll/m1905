"""
    将1970年到2050年中的闰年，存入列表．
"""
# list_leap_year = []
# for i in range(1970, 2051):
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         list_leap_year.append(i)
#
# for i in range(len(list_leap_year)):
#     print(list_leap_year[i], end=",")
#     if (i+1) % 5 == 0:
#         print()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
    存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
"""
# dict_city_info = {
#     "北京": {"景区": ["故宫", "天安门", "天坛"],
#            "美食": ["烤鸭", "炸酱面", "豆汁", "卤煮"]},
#     "四川": {"景区": ["九寨沟", "峨眉山", "春熙路"],
#            "美食": ["火锅", "串串香", "兔头"]}
# }
# for name, info in dict_city_info.items():
#     print(name+":")
#     for k, v in info.items():
#         print("    "+k+":",end="")
#         print(",".join(v))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.
    
"""
# str01 = input("输入一个字符串：")
# dict_str_count = {}
# for i in str01:
#     if i not in dict_str_count.keys():
#         dict_str_count[i] = 1
#     else:
#         dict_str_count[i] += 1
#
# for k, v in dict_str_count.items():
#     print(k,v)

# 1 2 3 4 5 6 7 8 9 10 11 12

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
    三色球问题，红球3个，黄球3个，绿球6个，
    任意取 8 个球，共有几种可能
"""
# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 7):
#             if i + j + k == 8:
#                 print("拿红球%d个，黄球%d个，绿球%d个" % (i, j, k))
