from concurrent.futures import ProcessPoolExecutor
import datetime
import logging


logging.basicConfig(level=logging.INFO, format='%(process)d %(processName)s %(thread)s %(message)s')

def worker(n):
    s= 0
    for _ in range(n):
        s += 1
    return s

if __name__ == '__main__':
    t = []
    with ProcessPoolExecutor(3) as P_executor:  # prepare 3 processes in pool ;it has __enter__ and __exit__
        start = datetime.datetime.now()
        for i in range(3):
            ts = P_executor.submit(worker,100000000)
            t.append(ts)
        for thr in t :
            flag = True
            if not thr.done:
                flag = False
                break
            if flag:
                logging.info('result : {}'.format(thr.result()))
        delta = (datetime.datetime.now() - start).total_seconds()
        logging.info('running time : {}'.format(delta))
        print('===========end=================')