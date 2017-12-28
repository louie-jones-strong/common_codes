from multiprocessing import Process
from kernels import f as f


def split_task():
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

split_task()