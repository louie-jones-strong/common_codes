from multiprocessing import Pool

def split_task( input_array , num_of_threads , kernel ):
    
    pools = Pool(num_of_threads)
    outputs = pools.map( kernel , input_array )

    return outputs