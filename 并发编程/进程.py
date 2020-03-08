from multiprocessing import Process
import time
def myThreading():
    time.sleep(2)
    print('子线程正在运行',time.ctime())

def myThreading1():
    time.sleep(4)
    print('子线程1正在运行',time.ctime())


if __name__ == '__main__':
    q = Process(target=myThreading)
    q1 = Process(target=myThreading1)

    # q.daemon
    # q1.daemon

    q.start()
    q1.start()

    # q.join()
    # q1.join()

    print('主线程正在运行',time.ctime())

# #开进程的方法一:
# import time
# import random
# from multiprocessing import Process
# def piao(name):
#     print('%s piaoing' %name,time.ctime())
#     time.sleep(2)
#     print('%s piao end' %name,time.ctime())
#
#
# if __name__ == '__main__':
#
#     p1=Process(target=piao,args=('egon',)) #必须加,号
#     p2=Process(target=piao,args=('alex',))
#     p3=Process(target=piao,args=('wupeqi',))
#     p4=Process(target=piao,args=('yuanhao',))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#     print('主线程',time.ctime())



# from multiprocessing import Process
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     global n
#     n=0
#     print('子进程内: ',n)
#
# #进程直接的内存空间是隔离的
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)