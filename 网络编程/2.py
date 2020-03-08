import socket
import subprocess

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port_ip = ('127.0.0.1',8000)

tcp_client.connect(port_ip)

#通讯循环
while True:
    msg = input('>>')
    tcp_client.send(msg.encode('utf-8'))
    print('成功发送信息：',msg)

    feedback = tcp_client.recv(10000)
    print('成功接收到反馈信息',feedback.decode('gbk'))

