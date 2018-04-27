from threading import Thread, Event
from queue import Queue
import threading
import time
import random

class producer(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        for i in range(10):
            self.queue.begin_task()
            item = random.randint(0,256)
            print('Producer notify:item N°%D appendend to queue by %s\n\%(item,self.name)')
            self.queue.task_done()
            time.sleep(1)

class consumer(Thread):
    def __init_(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            self.queue.begin_task()
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s\%(item,self.name)')
            self.queue.task_done()
class listClass:    
    

    def __init__(self):
        self.lista = []
        self.lock = threading.RLock()
    def add(self,item):
        self.lista.append(item)
    def get(self):
        if self.lista:
            last = self.lista[0]
            del self.lista[0]
        else:
            return None
        return last
    def begin_task(self):
        self.lock.acquire()
    def task_done(self):
        self.lock.release()


if __name__ == '__main__':
    lista = listClass()
    t1 = producer(lista)
    t2 = consumer(lista)
    t3 = consumer(lista)        
    t4 = consumer(lista)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
