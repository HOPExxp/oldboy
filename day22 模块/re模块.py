import re
#
# a = re.findall('a[bcd]l','ablcal')
# print(a)


print(re.findall("a(bc)|(gd)","abcdefgd"))
print(re.search("ab(bc)|(gd)","abbcgddefgd").group())


l = []
l.append()