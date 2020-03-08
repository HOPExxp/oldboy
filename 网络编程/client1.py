import socket

#买手机  --  套接字家族 | 端口协议
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#直接打电话  连接服务端  --  给一个地址- ip | 端口号
phone.connect(('127.0.0.1',1001))
#实现多次发送信息
while True:
    #自定义一条信息
    msg = input('输入一条信息：')
   #若信息为空，会导致程序卡死，用if判断跳过此情况
    if not msg:
        continue
    # 接通电话后发信息
    phone.send(msg.encode('utf-8'))
    print('向服务端发送信息：',msg)
    # #接收完整信息
    # accept = 0
    # server_accept = len(msg)
    #接收反馈信息  指定一次接收的量
    data = phone.recv(10)
    print('成功接收到服务端反馈信息 ')
#关机
phone.close()