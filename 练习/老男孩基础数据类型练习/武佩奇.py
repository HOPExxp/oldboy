# 一、元素分类
#
# 有如下值集合[11, 22, 33, 44, 55, 66, 77, 88, 99, 90...]，将所有大于
# 66
# 的值保存至字典的第一个key中，将小于
# 66
# 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
#

# k = {
#     'k1':[],
#     'k2':[]
# }
#
# l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# for i in l:
#     if i > 66:
#         k['k1'].append(i)
#     else:
#         k['k2'].append(i)
# print(k)


# 二、查找
# 查找列表中元素，移除每个元素的空格，并查找以
# a或A开头
# 并且以
# c
# 结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
for i,j in enumerate(li) :
    s = j.strip()
    li[i] = s
# print(li)
# for i in li :
#     if (i.startswith('a') and i.endswith('c')) or (i.startswith('A') and i.endswith('c')) :
#         print(i)

tu = ("alec", " aric", "Alex", "Tony", "rain")
n = list(tu)
for i,j in enumerate(tu) :
    m = j.strip()
    # print(m)
    n[i] = m
# print(tuple(n))

dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
for i in dic:
    dic[i] = dic[i].strip()
# print(dic)


# 三、输出商品列表，用户输入序号，显示用户选中的商品
# 商品
li = ["手机", "电脑", '鼠标垫', '游艇']
for i,j in enumerate(li) :
    print("{:<5}{:<10}".format(i,j))
f = input("请输入序号>>")
print(li[int(f)])