from multiprocessing import Pool
from kernels import f as f
import time

def split_task( input_array , ):
    pools = Pool(10)
    output = pools.map( f , num )

    return output