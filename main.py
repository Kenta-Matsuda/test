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

# 辞書型の学習用
def for_dict():
    d = {i:'odd' if i%2 else 'even' for i in range(1,4)}
    # keyのみ取得される
    for i in d:
        print(i)
        # 1
        # 2
        # 3
    
    # 単純なfor文の場合と同様で、keyのみ取得される    
    for i in d.keys():
        print(i)
        
    # valueのみ取得される
    for i in d.values():
        print(i)
        
    # key, valueの両方を取得する
    for i, j in d.items():
        print(i,j)
        
    for i in d.items():
        print(i)
    
# 内包表記の学習用
def comprehension():
    x_list = [4,5,6]
    for x in x_list:
        print('{} is divisible by 6'.format(x) if x%6==0 else
              '{} is divisible by 3'.format(x) if x%3==0 else
              '{} is divisible by 2'.format(x) if x%2==0 else
              '{} is not divisible by 2 or 3'.format(x))

if __name__=='__main__':
    # multiThreads()
    # multiArgs([1,'taro',lambda:print('test')])
    # for_dict()
    # comprehension()


# セルの実行    
# In[1]