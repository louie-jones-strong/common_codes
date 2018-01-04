from multiprocessing import Pool
import importlib
#from kernels import f as f

def split_task( input_array , num_of_threads , kernel ):
    
    test = importlib.import_module( "kernels" )
    test = test.f()

    pools = Pool(num_of_threads)
    outputs = pools.map( test , input_array )

    return outputs