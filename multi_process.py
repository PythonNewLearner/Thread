import multiprocessing
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(process)d %(processName)s %(thread)s %(message)s')


def calc(c):
    s = 0
    for _ in range(c):
        s += 1
    return s


if __name__ == '__main__':
    start = datetime.datetime.now()

    pool = multiprocessing.Pool(5)  # we will use 5 processors
    for i in range(5):  # we run 5 processes 
        pool.apply_async(calc, args=(1000000000,), callback=lambda s: logging.info('s = {}'.format(s)))

    pool.close()
    pool.join()

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)
