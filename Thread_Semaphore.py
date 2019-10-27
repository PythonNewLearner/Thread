from threading import Thread,Semaphore,BoundedSemaphore
import threading
import logging

FORMAT= '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

class Conn:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name

class Pool:
    def __init__(self,count):
        self.count = count
        self.pool = [self._connect('worker - {}'.format(x)) for x in range(count)]
        self.sema = BoundedSemaphore(count)  # Semaphore with a bound with count

    def _connect(self,name):
        return Conn(name)

    def get(self):       #get a element from the pool
        self.sema.acquire()  # lock and value will decrease by 1
        return self.pool.pop()

    def return_conn(self,conn:Conn):  # return a element to the pool
        self.pool.append(conn)
        self.sema.release() #release and value will increase by 1 but bounded to count

pool = Pool(10)    # only have 10 resources
def worker(pool):
    conn = pool.get()
    logging.info(conn)
    threading.Event().wait(2)
    pool.return_conn(conn)

for i in range(20):   # there are 20 threads will get and return the resources
    Thread(target=worker,args=(pool,)).start()

print('======end===============')

#Difference between Lock and Semephore: Lock is used when only One resource is available but Semaphore can be used when we have limited multiple resources