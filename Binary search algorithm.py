"""
In binary search algorithm we required a sorted list
only mid value is compare with key value(the value which is searched in the list)
"""

############ Binary search algorithm using iterative method ##############

# def binarysearch (A, key) :
#     low = 0
#     high = len(A)-1
#     while low <= high :
#         mid = (low + high) // 2
#         if A[mid] == key :
#             return True
#         elif A[mid] > key :
#             high = mid -1
#         else :
#             low = mid + 1
#     return False
#
# l=[15,21,47,84,96]
# print(binarysearch(l, 51))

############ Binary search algorithm using recursive method ##############

def binarysearchrecursive (A, key, low, high) :
    if low > high :
        return False
    else :
        mid = (low + high) //2
        if A[mid] == key :
            return True
        elif A[mid] > key :
            return binarysearchrecursive(l, key, low, mid -1)
        else :
            return binarysearchrecursive(l, key, mid +1, high)

l=[15,21,47,84,96]
print(binarysearchrecursive(l, 69, 0, 4))