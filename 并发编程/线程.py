import threading
import time
def myThreading():
    time.sleep(2)
    print('子线程正在运行',time.ctime())

def myThreading1():
    time.sleep(4)
    print('子线程1正在运行',time.ctime())


if __name__ == '__main__':
    q = threading.Thread(target=myThreading)
    q1 = threading.Thread(target=myThreading1)
    #
    # q.setDaemon(True)
    # q1.setDaemon(True)

    q.start()
    q1.start()

    # q.join()
    # q1.join()

    print('主线程正在运行',time.ctime())


# import threading
# import time
#
#
# class myThreading(threading.Thread):
#     # time.sleep(2)
#     # print('子线程正在运行')
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         time.sleep(2)
#         print('子线程{}正在运行'.format(self.name))
#
# class myThreading1(threading.Thread):
#     # time.sleep(4)
#     # print('子线程1正在运行')
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#     def run(self):
#         time.sleep(4)
#         print('子线程{}正在运行'.format(self.name))
#
# if __name__ == '__main__':
#     q = myThreading(1)
#     q1 = myThreading1(2)
#
#     # q.setDaemon(True)
#     # q1.setDaemon(True)
#
#     q.start()
#     q1.start()
#
#     # q.join()
#     # q1.join()
#
#     print('主线程正在运行')



# import threading
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
# def work():
#     global n
#     n=0
#     print('子进程内: ',n)
#
# #线程直接的内存空间是共享的
# if __name__ == '__main__':
#     p=threading.Thread(target=work)
#     p.start()
#     print('主进程内: ',n)