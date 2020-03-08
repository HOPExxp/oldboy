# a = str('abcd efgh')
# print(type(a))
#
# #首字母大写  capotalize只大写第一个字母；title大写每个单词的首字母
# print(a.capitalize())
# print(a.title())
#
#
# #全部小写  lower只适用于英文字母，casefold也适用于其他语言
# print(a.lower())
# print(a.casefold())
#
# #全部大写
# print(a.upper())
#
# #计数字符串的字符数
# print(a.count())
#
# #将字符串置中   第一个参数指定总长度，第二个参数指定填充的字符
# print(a.center(10,'-'))

a = 'asd   中'
# print(a.isalpha())

# print(a.isprintable())
v=a.replace('a','d')
print(v)