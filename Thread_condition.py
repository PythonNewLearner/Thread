from threading import Condition,Thread,Lock,Event
import logging
import random

FORMAT= '%(asctime)s %(threadName)s %(thread)d %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
class Dispatcher:
    def __init__(self):
        self.data = None
        self.cond = Condition()
        self.event = Event()

    def produce(self, total):
        for _ in range(total):
            self.data = random.randint(0, 100)
            with self.cond:
                self.cond.notify_all()
                logging.info(self.data)
            self.event.wait(1)

    def consume(self):
        while True:
            with self.cond:
                self.cond.wait()  #wait to receive data from produce
                logging.info(self.data)
            self.event.wait(0.5)


d = Dispatcher()
p = Thread(target=d.produce, args=(10,),name='producer')


for i in range(3):  #run 3 threads on consume
    c = Thread(target=d.consume,name='consumer')
    c.start()
p.start()

print("end==============")