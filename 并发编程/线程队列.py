import threading
import time
import queue
def myThreading():
    time.sleep(2)
    print('子线程正在运行')
    p.put('子')

def myThreading1():
    time.sleep(4)
    print('子线程1正在运行')
    p.put('子1')


if __name__ == '__main__':
    p = queue.Queue ()
    q = threading.Thread(target=myThreading)
    q1 = threading.Thread(target=myThreading1)

    # q.setDaemon(True)
    # q1.setDaemon(True)

    q.start()
    q1.start()
    print(p.get())
    # q.join()
    # q1.join()

    print('主线程正在运行')
