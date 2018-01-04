from multiprocessing import Process
import threading
import subprocess
from kernels import f as f


def split_task():
    print("test")
    if __name__ == '__main__':
        num = [[1],[2]]
        p = num

        p[0] = Process(target=f, args=(num[0]))
        p[1] = Process(target=f, args=(num[1]))

        p[0].start()
        p[1].start()

        p[0].join()
        p[1].join()

        print(num)

    return

def split_task2():


    worker = threading.Thread(target=f, name=loop , args=(arg,))
    worker.start()

    worker.join()
    return

def split_task3(input):
    output = list(map(lambda x: f(x) , input ))
    return output

def split_task4():
    print("hello")
    cmd = "python email.py"
    subprocess.run(cmd)
    subprocess.Popen()
    #output = subprocess.CompletedProcess(cmd,returncode=0)
    #print(output)
    print("test")
    return

split_task4()