import socket

#买手机  --  套接字家族 | 端口协议
phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#服务端地址
ip_port = ('127.0.0.1',8001)
#实现多次发送信息
while True:
    #自定义一条信息
    msg = input('输入一条信息：')
   #若信息为空，会导致程序卡死，用if判断跳过此情况
    if not msg:
        continue
    # 接通电话后发信息  指定数据 和 服务端地址
    phone.sendto(msg.encode('utf-8'),ip_port)
    print('向服务端发送信息：',msg)
    #接收反馈信息  指定一次接收的量
    data,addr = phone.recvfrom(10)
    print('成功接收到服务端反馈信息 ')
#关机
phone.close()


#tcp:
#报错
#输入数据的长度大于最大接收长度
#信息是否为空
#强行断开客户端导致服务端抛出异常