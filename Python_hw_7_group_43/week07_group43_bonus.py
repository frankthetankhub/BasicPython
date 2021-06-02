# Task 7. Bonus Task - enumerate()
## Task 7. Bonus Task 1 - Multiply
def multiply(list):
    for i,e in enumerate(list):
        list[i] = e*i
    return list

## Task 7. Bonus Task 2 - dot product
def dot_product(list1, list2):
    product = 0
    for i,e in enumerate(list1):
        product += e * list2[i]
    return product

### testing results
print(multiply([5,6,8]))
print(dot_product([2,4,5], [1,3,4]))
