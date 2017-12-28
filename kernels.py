import time
import os

def f(n):
    print("test4")
    time_mark = time.time()
    for loop in range(100):
        if n == 1:
            os.system("title "+str(loop)+"/100")
        time.sleep(0.02)
    print("thread_"+str(n)+" is done in: "+ str(time.time()-time_mark))
    return n*n