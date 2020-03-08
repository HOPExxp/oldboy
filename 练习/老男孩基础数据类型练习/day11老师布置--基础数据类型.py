# #encoding = Unicode
# s = u'子杰'
# print(s)
# print(type(s))
#
# u = s.encode('utf-8')
# print(u)
# print(type(u))
# '''
# u1 = s.encode('gbk')
# print(u1)
# print(type(u1))
# '''
#
# a = '子杰'.encode('utf-8')
# print(a)
# b = b'abc'
# print(type(b))


# n1 = 5
# print(bin(n1))
#
# print(n1.bit_length())


# a = "alex"
# b = a.capitalize()
# print(a)
# print(b)


#10   写代码，实现下列功能
# name = "aleX"
# #a移除name变量对应的值的两边的空格
#
# print(name.strip())
#
# print(name.startswith('al'))
#
# print(name.endswith('X'))
#
# print(name.replace('l','p'))
#
# print(name.partition('l'))
#
# print(name.upper())
#
# print(name.lower())
#
# print(name[1])
#
# print(name[:3])
#
# print('----')
# print(name.find('e'))
#
# print(name[:-1])


# a = 'jiwjsaj'
# for i in a:
#     print(i)


#
# a = 'skfjeiae'
# # a = ['a','b','c']
# b = "_".join(a)
# print(b)


#24.整数加法计数器
# content = input("请输入内容：")
# a = content.split('+')
# sum = 0
# for i in a:
#     sum += eval(i)
# print(sum)

#25.计算用户输入的内容中有几个十进制数字？几个字母？
# content = input("请输入内容：")
# num = 0
# alpha = 0
# for i in content:
#     if i.isdecimal():
#         num += 1
#     if i.isalpha():
#         alpha += 1
# print('num:', num ,'alpha:', alpha)

#27.等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意显示
#   如敬爱可亲的***，最喜欢在***地方干***
# while True:
#     name = input('请输入名字：')
#     hobby = input('请输入爱好：')
#     place = input('请输入地点：')
#     print('幼稚的{}最喜欢在{}干{}'.format(name,place,hobby))

#29.开发敏感词过滤程序，提示用户输入内容，如果输入的内容包含特殊字符：
#如’苍老师‘’东京热‘，则将内容替换为’****‘

# 法一
result = ''
content = input("请输入内容：")
if '苍老师' in content:
    content = content.replace('苍老师','***')
if '东京热' in content:
    content = content.replace('东京热','***')
print(content)

#法2
# result = ''
# content = input("请输入内容：")
# limt = ['苍老师','东京热']
# for i in limt:
#     if i in content:
#         result = content.replace(i,'***')
# print(result)
#
# a = 'abcd'
# b = a.replace('a','c')
# print(b)

#30.制作表格
#循环提示用户输入：用户名、密码、邮箱（要求输入的长度不超过20个字符，如果超过只取前20位）
#如果用户输入Q /q 表示不再继续输入，将用户输入的内容以表格形式打印
# li = []
# s = ''
# while True:
#     name = input('请输入用户名：')
#     if name.lower() == 'q':
#         break
#     nima = input('请输入密码：')
#     if nima.lower() == 'q':
#         break
#     youxiang = input('请输入邮箱：')
#     if youxiang.lower() == 'q':
#         break
#     single = '{0}\t{1}\t{2}\n'.format(name,nima,youxiang)
#     s += single
# print(s.expandtabs(20))
    # single = '用户名：{:<25} 密码：{:<25} 邮箱：{:<25}'.format(name,nima,youxiang)
    # li.append(single)
# for i in li:
#     print(i)


#28.制作随机验证码
#流程：  --用户执行程序
#        --给用户显示需要输入的验证码
#        --用户输入值
#             用户输入的值和显示的值相同时显示正确信息，否则继续生成随机验证码继续等待用户输入

# def check_code():
#     import random
#     checkcode = ''
#     for i in range(4):
#         current = random.randrange(0,4)
#         if current != i:
#             #ascii 65-90 对对应大写英文字母
#             temp = chr(random.randint(65,90))
#         else:
#             temp = random.randint(0,9)
#         checkcode += str(temp)
#     return checkcode
# while True:
#     code = check_code()
#     print(code)
#     answer = input('现在输入你的验证码值：')
#     if answer == code:
#         print('验证通过')
#         break
#     else:
#         continue