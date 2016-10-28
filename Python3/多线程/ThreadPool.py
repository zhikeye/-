# -*- coding: utf-8 -*-
__auth__ = 'yzk'
'''
简单的线程管理
'''

import threading
import queue


class WorkerThread(threading.Thread):
    """"""
    def __init__(self,requestQueue,resultQueue,poolTimeOut=5,**kwds):
        threading.Thread.__init__(self,**kwds)
        '''设置为守护进程'''
        self.setDaemon(True)
        self._requestQueue = requestQueue
        self._responeQueue = resultQueue
        self._poolTimeOut = poolTimeOut
        '''设置一个flag信号，用来表示该线程是否还被dismiss,默认为false'''
        self._dismiss = threading.Event()
        self.start()

    def run(self):
        while True:
            if self._dismiss.is_set():
                break
            try:
                request = self._requestQueue.get(True,self._poolTimeOut)
                if self._dismiss.is_set():
                    self._requestQueue.put(request)
                    break

                print(request)
                c = request[0] + request[1]
                self._responeQueue.put(int(c))
            except Exception as e:
                print(e)



    def dismiss(self):
        '''设置一个标志，表示完成当前work之后，退出'''
        self._dismiss.set()


class ThreadPool():
    def __init__(self,threadNum=5,timeOut =5):
        print('ThreadPool start')
        self._threadNum = threadNum
        self._timeOut = timeOut
        self._requestQueue = queue.Queue()
        self._responeQueue = queue.Queue()
        self._workers = []

    def createWorker(self):
        for i in range(self._threadNum):
            self._workers.append(WorkerThread(self._requestQueue,self._responeQueue,poolTimeOut=self._timeOut))

    def add(self,q):
        self._requestQueue.put(q)

    def getRespone(self):
        if self._responeQueue.empty():
            return None
        else:
            return self._responeQueue.get()

    def join(self):
        for o in self._workers:
            o.join()

if __name__ == '__main__':
    pool = ThreadPool()
    pool.createWorker()
    pool.add([5,8])
    pool.add([9,10])
    pool.add([15,20])
    while True:
        if pool._responeQueue.empty():
            pass
        else:
            print(pool._responeQueue.get())
    pool.join()
