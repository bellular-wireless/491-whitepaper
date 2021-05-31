
from sys import flags
import heap_sort
import merge_sort
import merge_sort_threads
import random
from datetime import datetime
import tracemalloc
import io

def gen_array(max, len) :
    arr = []
    for i in range(len) :
        arr.append(random.randrange(max))
    return arr

def sort_with_alg(sorter, size) :
    A = gen_array(100, size)
    start = datetime.now()
    tracemalloc.start()
    sorter(A)
    memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    end = datetime.now()
    del A
    return ((end - start).total_seconds(), memory)

if __name__ == '__main__':
    sort_with_alg(heap_sort.heap_sort, 50000)
    sort_with_alg(merge_sort_threads.merge_sort, 50000)
    sort_with_alg(merge_sort.merge_sort, 50000)
    time = open("time.csv", "w")
    time.write("n,merge_sort,merge_sort_threads,heap_sort\n")
    memory = open("memory.csv", "w")
    memory.write("n,merge_sort,heap_sort\n")

    for i in range(50000, 500001, 50000) :
        print(i)
        metrics_ms = sort_with_alg(merge_sort.merge_sort, i)
        metrics_ms_t = sort_with_alg(merge_sort_threads.merge_sort, i)
        metrics_hs = sort_with_alg(heap_sort.heap_sort, i)
        time.write("{:d},{:f},{:f},{:f}\n".format(i, metrics_ms[0], metrics_ms_t[0], metrics_hs[0]))
        memory.write("{:d},{:d},{:d}\n".format(i, metrics_ms[1], metrics_hs[1]))
    print("done!")
