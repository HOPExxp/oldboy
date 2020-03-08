# tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
# print(tpl)
# tp2 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
# print(tp2)
# tp3 = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
# print(tp3)
# tp4 = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
# print(tp4)
# tp5 = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)
# print(tp5)

tpl = "i am {:-^20}, age {:^10,.2f}, {}".format("seven", 18, 'alex')
print(tpl)

