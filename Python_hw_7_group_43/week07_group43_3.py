# Task 7.3 - Style
## Task 7.3.1 - Implementing Pseudocode with Good Style
def counting_sort(L, m):
    S = []
    ### create list for Counts of size m+1 with 0 as all entries
    C = [0] * (m + 1)

    ### increase the count at the index of the number in C
    for v in L:
        C[v] += 1

    for i,c in enumerate(C):
        ### add the number as often as it is counted to S
        while c > 0:
            S.append(i)
            c -= 1

    return S

### test with given list
list = [4, 9, 2, 4, 1, 1, 5, 1, 0, 0, 9]
print(counting_sort(list, 9))
