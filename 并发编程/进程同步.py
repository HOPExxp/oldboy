from multiprocessing import Process, Lock
# from threading import Thread,Lock
import threading
def f(l, i):
    # with l.acquire():
        print('hello world %s' % i)


if __name__ == '__main__':
    lock = Lock()
    lock1 = threading.Lock
    # for num in range(10):
    #     Process(target=f, args=(lock, num)).start()
    for num in range(10):
        threading.Thread(target=f, args=(lock1, num)).start()