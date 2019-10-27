from threading import Condition,Thread,Lock,Event,Barrier
import threading
import logging



FORMAT= '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)

bar = Barrier(3) #number of parties,every 3 threads will start work

def worker(bar:Barrier):
    logging.info("I am working-Number of waiting: {}".format(bar.n_waiting)) # numbers of threads stuck at barrier: once it;s 3, it will start
    try:
        bar.wait()  # if timeout, barrier will abort and broken
    except threading.BrokenBarrierError:
        logging.info('Broken Error')
    logging.info("Job done - Number of waiting: {}".format(bar.n_waiting))


for i in range(10): #10 threads
    if i ==2 :
        bar.abort()  #abort: barrier is broken.
    if i == 4:
        bar.reset()  #reset barrier
    Thread(target=worker,args=(bar,),name='Barrier').start()

print('=====end========')