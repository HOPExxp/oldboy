import socket

#买手机  --  套接字家族 | 端口协议
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#买电话卡  --  监听一个地址- ip | 端口号
phone.bind(('127.0.0.1',1001))

#开机  指定监听的最大数量   **backlog -- 半连接池**所有的电话均在其中等待
phone.listen(5)
#使得服务端完成一次连接后可继续和第二人连接，多次accept
while True:
    #等电话-接电话  电话接通后会得到(return sock, addr)   accept() -> (socket object, address info)
    #tcp链接  |  客户端地址？
    print('等待连接')
    link, addr = phone.accept()    #    **从backlog中拿出一个电话接通**
    #多次接发信息　　
    while True:
        #当一个客户端完成通信后客户端主动断开时会导致服务器抛出异常
        try:
            #电话接通后接收信息  指定一次接收信息的数量
            data = link.recv(10)
            print('接受到客户端信息为： ',data)
            #接收到信息后，反馈给client端一个信息，以告诉他已成功接收
            link.send(data)
            print('成功向客户端发送一个反馈信息')
        except Exception:
            break
        #完成一切操作后关掉link，再关机
    link.close()
phone.close()