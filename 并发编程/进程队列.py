# #方法一  进程队列 Queue
# from multiprocessing import Process,Queue
#
# def f(q,i):
#     q.put(i**2)
#     print('son process ',id(q))
#
# if __name__ == '__main__':
#     q = Queue()
#     print('main process ',id(q))
#
#     p1 = Process(target=f,args=(q,1,))
#     p1.start()
#     p2 = Process(target=f,args=(q,2,))
#     p2.start()
#     p3 = Process(target=f,args=(q,3,))
#     p3.start()
#
#     print(q.get())
#     print(q.get())
#     print(q.full())

# 方法二
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([12, {"name":"yuan"}, 'hello'])
    response=conn.recv()
    print("response",response)
    conn.close()
    print("q_ID2:",id(conn))

if __name__ == '__main__':

    parent_conn, child_conn = Pipe()
    print("q_ID1:",id(child_conn))
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    parent_conn.send("儿子你好!")
    # p.join()

#方法三 Manager
from multiprocessing import Process, Manager

def f(d, l,n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    #print(l)

    print("son process:",id(d),id(l))

if __name__ == '__main__':

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        print("main process:",id(d),id(l))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d,l,i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
