import threading
from logging import getLogger
import os

logger = getLogger(__name__)
__auther__="matsuda kenta"

# *args変数の学習用
def multiArgs(*args):
    logger.debug('Start multiArgs method')
    print(args)

# マルチスレッド処理の学習用
def multiThreads():
    logger.debug('Start multiThreads method')
    logger.info('Thread {} is now working'.format(threading.current_thread().name))

    numCPU = os.cpu_count()
    logger.debug('{} cpu cores are now available'.format(numCPU))
    
    logger.debug('Generate {} threads'.format(numCPU))
    threads = [threading.Thread(target=lambda i: print('スレッド {}'.format(i + 1)), args=(i,)) for i in range(10)]

    for thread in threads:
        thread.start()
        thread.join()

if __name__=='__main__':
    multiThreads()