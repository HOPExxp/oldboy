# import threading
# from time import ctime,sleep
# import time
#
# def ListenMusic(name):
#
#         print ("Begin listening to %s. %s" %(name,ctime()))
#         sleep(3)
#         print("end listening %s"%ctime())
#
# def RecordBlog(title):
#
#         print ("Begin recording the %s! %s" %(title,ctime()))
#         sleep(5)
#         print('end recording %s'%ctime())
#
#
# threads = []
#
#
# t1 = threading.Thread(target=ListenMusic,args=('水手',))
# t2 = threading.Thread(target=RecordBlog,args=('python线程',))
#
# threads.append(t1)
# threads.append(t2)
#
# if __name__ == '__main__':
#
#     for t in threads:
#         #t.setDaemon(True) #注意:一定在start之前设置
#         t.start()
#         #串行
#         # t.join()
#     #等线程
#     # t1.join()
#     # t1.setDaemon(True)
#
#     #t2.join()########考虑这三种join位置下的结果？
#     print ("all over %s" %ctime())


import threading
import time
def myThreading():
    time.sleep(2)
    print('子线程正在运行',time.ctime())

def myThreading1():
    time.sleep(4)
    print('子线程1正在运行',time.ctime())


if __name__ == '__main__':
    q = threading.Thread(target=myThreading,group=5)
    # q1 = threading.Thread(target=myThreading1)
    #
    # q.setDaemon(True)
    # q1.setDaemon(True)
    for i in range(100):
        q.start()
    # q1.start()

    # q.join()
    # q1.join()

    print('主线程正在运行',time.ctime())