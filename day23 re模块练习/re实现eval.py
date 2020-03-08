# "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
import re

# str = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

# s = str.replace(' ','')
# if s.count('(') == s.count(')'):
#     li = re.findall('\([^()]+\)',str)
#     for l in li:
#         fuhao = re.findall('\+|-|\*|/',l)
#         shuzhi = re.findall('\d+',l)
#         print(l)
#         print(fuhao)
#         print(shuzhi)



#******************************************************实现单个括号的算法

st = "(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )"
s = st.replace(' ','')
# chengchu = re.findall('(?:\d+(?:\*|/))+\d+',s)    #['2*5/3', '7/3*99/4*2998', '10*568/14']
chengchu = re.findall('(?:\d+[*/])+\d+',s)      #['2*5/3', '7/3*99/4*2998', '10*568/14']
print(chengchu)


#先计算优先的乘除法，再将结果再源字符串中替换，最后实现加减法

#i 即为每个乘除算式
for j,i in enumerate(chengchu):
    #每次算一个（一个算式可能有多个乘除）
    while re.search('\d+[*/]\d+',i):
        res = re.search('\d+[*/]\d+',i).group()
        # print(res)
        #算完后将结果替换原算式
        i = i.replace(res,str(eval(res)),1)
        # i = i.replace(res,str("{:.2f}".format(eval(res))))
        #继续下次算法
    # print(i)
    s = s.replace(chengchu[j],str(i))
    #sub方法  错误
    # s = re.sub('(?:\d+[*/])+\d+',str(i),s)
    # 2*5
    # 10/3
    # 3.3333333333333335
    # ！！？！！7/3
    # ！！？！！3333333333333335*99
    # ！！？！！330000000000000165/4
    # ！！？！！16*2998
    # ！！?！！2.8.250000000000005e+47968
    # 10*568
    # 5680/14
    # 405.7142857142857
print(s)




#****************************************************** 实现单个括号算法

#eval 算法直接实现***************************************

# for i,j in enumerate(chengchu):
#     # s = s.replace(chengchu[i],str(eval(j)))   #(9-3.3333333333333335+173134.50000000003+405.7142857142857)
#     s = s.replace(chengchu[i], str("{:.2f}".format(eval(j))))
# print(s)




