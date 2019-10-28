from concurrent.futures import ThreadPoolExecutor
import time
import logging
import random

logging.basicConfig(level=logging.INFO, format='%(process)d %(processName)s %(thread)s %(message)s')

def worker(n):
    logging.info('start working'.format(n))
    time.sleep(2)
    logging.info('finish work'.format(n))
    return random.randint(1,10)

if __name__ == '__main__':
    t = []
    with ThreadPoolExecutor(3) as T_executor:  # prepare 3 threads in pool ;it has __enter__ and __exit__
        for i in range(3):
            ts = T_executor.submit(worker,i)
            t.append(ts)
        for thr in t :
            flag = True
            if not thr.done:
                flag = False
                break
            if flag:
                logging.info('result : {}'.format(thr.result()))

        print('===========end=================')