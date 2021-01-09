def linearsearch(A, key) :
    ans = "False"
    for i in range (len(A)) :
        if A[i] == key :
            ans = 'True'
            break
    return ans
A = [84,21,47,96,15]
print(linearsearch(A,96))