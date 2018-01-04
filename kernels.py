import time
import os


def f(n):
    n = n[0]
    time_mark = time.time()
    for loop in range(100):
        if n == 1:
            os.system("title "+str(loop)+"/100")
        time.sleep(0.02)
    print("thread_"+str(n)+" is done in: "+ str(time.time()-time_mark))
    n = n*n
    print(n)
    return n