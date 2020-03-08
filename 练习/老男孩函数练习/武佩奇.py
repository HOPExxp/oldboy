# 1、简述普通参数、指定参数、默认参数、动态参数的区别
#        位置参数  关键字参数 给定默认值  不定长参数

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
#
# def count_num():
#     string = input('输入字符串>>')
#     sum_num = len(string)
#     dig = 0
#     alp = 0
#     spa = 0
#     oth = 0
#     for i in string:
#         if i.isdigit():
#             dig += 1
#         elif i.isalpha():
#             alp += 1
#         elif i.isspace():
#             spa += 1
#         else:
#             oth += 1
#     print('总个数{:<5}数字个数{:<4}字母个数{:<4}空格个数{:<4}其他类型{:<4}'.format(sum_num,dig,alp,spa,oth))
#
# count_num()

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
#
# def charge_len():
#     obj = input('>>')
#     length = len(obj)
#     if length > 5:
#         print('该对象的长度大于5')
#     else:
#         print('该对象的长度效于5')
# charge_len()

# 4、写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
#
# def check_space():
#     s = input('>>')
#     res = '含有空内容' if ' ' in s else '不含空内容'
#     print(res)
# check_space()

# 5、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
# def cut():
#     l = eval(input('>>'))
#     if len(l) > 2 :
#         l = l[:2]
#     return l
# res = cut()
# print(res)

# 6、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#
# def ji(l):
#     li = []
#     for i in l[::2]:
#         li.append(i)
#     return li
# lis = ['1','2','3','4','5','6','7']
# res = ji(lis)
# print(res)

# 7、写函数，检查传入字典的每一个value的长度, 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
# PS: 字典中的value只能是字符串或列表
#
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
#
# def check_len(di):
#     for i in di :
#         if len(di[i]) > 2 :
#             di[i] = di[i][:2]
#         else:
#             pass
#     return di
# d = check_len(dic)
# print(d)

# 8、写函数，利用递归获取斐波那契数列中的第10个数，并将该值返回给调用者。
#
# import sys
# sys.setrecursionlimit(20)


#******************************   ???
def func(arg1,arg2):
    if arg1 == 0:
        print(arg1)
        print(arg2)
    arg3 = arg1 + arg2
    print(arg3)
    func(arg3,arg2)

res = func(0,1)
