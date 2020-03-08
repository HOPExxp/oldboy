import socket
#实例化一个socket对象
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接的服务端地址
port_ip = ('127.0.0.1',8000)
#连接到服务端
tcp_client.connect(port_ip)

#通讯循环
while True:
    msg = input('>>')
    #对信息进行处理
    if not msg:continue
    if msg == 'quit':break
    #接通电话后发信息
    tcp_client.send(msg.encode('utf-8'))
    print('成功发送信息：',msg)
    #接收反馈信息
    feedback = tcp_client.recv(1000)
    print('成功接收到反馈信息',feedback.decode('gbk'))
#关闭连接
tcp_client.close()
