import socket

#买手机  --  套接字家族 | 端口协议
phone = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#买电话卡  --  监听一个地址- ip | 端口号
phone.bind(('127.0.0.1',8001))

#多次接发信息　　
while True:
    #电话接通后接收信息  指定一次接收信息的数量
    #返回数据 和 客户端地址
    data,addr = phone.recvfrom(10)
    print('接受到客户端信息为： ',data)
    #接收到信息后，反馈给client端一个信息，以告诉他已成功接收
    phone.sendto(data,addr)
    print('成功向客户端发送一个反馈信息')

    #完成一切操作后关掉link，再关机
link.close()
phone.close()