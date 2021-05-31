from math import floor
import threading
import multiprocessing

def merge_sort(A) :
    if len(A) > 1 :
        middle = len(A) // 2
        if len(A) > 20000 :
            left = []
            right = []
            left_thread = multiprocessing.Process(target=thread_wrapper, args=(A[:middle], left,))
            right_thread = multiprocessing.Process(target=thread_wrapper, args=(A[middle:], right,))
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()
        else :
            left = merge_sort(A[:middle])
            right = merge_sort(A[middle:])
        return merge(left, right)
    else :
        return A

def thread_wrapper(A, t) :
    t.extend(merge_sort(A))

def merge(A, B) :
    i, u = 0, 0
    result = []
    # merging
    while i < len(A) and u < len(B) :
        if A[i] < B[u] :
            result.append(A[i])
            i += 1
        else :
            result.append(B[u])
            u += 1
    
    # catching leftovers
    while i < len(A) :
        result.append(A[i])
        i += 1
    while u < len(B) :
        result.append(B[u])
        u += 1

    return result