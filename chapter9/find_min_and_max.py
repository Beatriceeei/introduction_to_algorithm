def find_min_and_max(A):
    length = len(A)
    if length == 1:
        return A[0], A[0]
    elif length == 2:
        return min(A), max(A)
    else:
        min1, max1 = find_min_and_max(A[:length/2])
        min2, max2 = find_min_and_max(A[length/2:])
        return min(min1,min2), max(max1, max2)

A = [5,4,6,3,3,23,5,1]
print find_min_and_max(A)