import multi_threading
import time


list = [0,1,2,3,4,5,6,7,8,9]

time_mark = time.time()
print(list)
output = multi_threading.split_task3(list)
print(output)
print(time.time()-time_mark)