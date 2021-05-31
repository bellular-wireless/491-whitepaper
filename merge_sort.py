from math import floor

def merge_sort(A) :
    if len(A) > 1 :
        middle = len(A) // 2
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:])
        return merge(left, right)
    else :
        return A

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