import socket
import subprocess

tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port_ip = ('127.0.0.1',8000)

tcp_server.bind(port_ip)

tcp_server.listen(3)

while True:
    conn,addr=tcp_server.accept()
    print('新的客户端链接',addr)
    while True:
        #收
        try:
            cmd=conn.recv(1000)
            if not cmd:break
            print('收到客户端的命令',cmd)

            #执行命令，得到命令的运行结果cmd_res
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()

            #发
            if not cmd_res:
                cmd_res='执行成功'.encode('gbk')
            conn.send(cmd_res)
        except Exception as e:
            print(e)
            break