
def left(i) :
    return i * 2 + 1
def right(i) :
    return i * 2 + 2
def parent(i) :
    return i // 2

def max_heapify(A, n, i) :
    largest_child = i
    if left(i) < n and A[largest_child] < A[left(i)] :
        largest_child = left(i)
    if right(i) < n and A[largest_child] < A[right(i)] :
        largest_child = right(i)
    
    if largest_child != i :
        A[i], A[largest_child] = A[largest_child], A[i]
        max_heapify(A, n, largest_child)

def heap_sort(A) :
    n = len(A)
    for i in range(n // 2 - 1, -1, -1) :
        max_heapify(A, n, i)
    for i in range(n - 1, 0, -1) :
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)