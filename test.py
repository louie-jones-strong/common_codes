import multi_threading
import time
import text_edits
import numpy

list = [[[1,2],3],[1,2,3],[1,2,3],[1]]
output = text_edits.array_to_text(list)
print(output)
input()

if __name__ == '__main__':
    time.sleep(1)
    list = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
    
    time_mark = time.time()
    print(list)
    from kernels import f as kernel
    output = multi_threading.split_task( list , 10 , kernel )
    print(output)
    print(time.time()-time_mark)