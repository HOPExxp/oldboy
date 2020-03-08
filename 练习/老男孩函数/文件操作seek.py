f = open('日志文件','rb')

for i in f:
    base = -10
    while True:
        f.seek(base,2)
        data = f.readlines()
        # print(data)
        if len(data) > 1:
            print('文件的最后一行：',data[-1].decode('utf-8'))
            break
        else:
            base *=2