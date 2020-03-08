import socket
import subprocess
#socket实例化一个对象
tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听的服务端地址
port_ip = ('127.0.0.1',8000)
#开启监听
tcp_server.bind(port_ip)
#设置最大监听数量
tcp_server.listen(3)

while True:
    #连接一个请求
    print('等待连接')
    sock,addr = tcp_server.accept()
    print('成功连接到',addr)
    #多次接发消息
    while True:
        # 当一个客户端完成通信后客户端主动断开时会导致服务器抛出异常
        try:
            # 电话接通后接收信息  指定一次接收信息的数量
            data = sock.recv(1000)
            print('接收到客户端的命令',data)
            #如果客户端发送的信息为空，使用此判断即可退出当前循环，不至于程序堵塞
            if not data:break
            #实现远程连接——连接到服务端的控制台命令台
            #可以通过通道PIPE进行数据传输
            proc = subprocess.Popen(
                #需要传输的数据
                data.decode('utf-8'),
                shell=True,
                #将标准输入放入通道
                stdin = subprocess.PIPE,
                # 将标准错误放入通道
                stderr = subprocess.PIPE,
                # 将标准输出放入通道
                stdout= subprocess.PIPE,
            )
            #从通道处拿出内容
            err = proc.stderr.read()
            if err:
                result_proc = err
            else:
                result_proc = proc.stdout.read()
            #如果程序有标准输出，但是又为空，就会没有反馈信息给客户端，引起客户端阻塞
            if not result_proc:
                result_proc = '执行成功'.encode('gbk')

            #*************************解决粘包
            # 接收到标准__信息后，反馈给client端，以告诉他已成功接收
            sock.send(result_proc)







            
        except Exception as e:
            print(e)
            break
    sock.close()
tcp_server.close()
