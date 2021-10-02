def countingSort(array):
    array_size = len(array)
    output = [0] * array_size

    # count array initialization
    count = [0] * 10

    # storing the count of each element 
    for i in range(0, array_size):
        count[array[i]] += 1

    # storing the count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # place the elements in output array 
    i = array_size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, array_size):
        array[i] = output[i]

data = [1,2,7,3,2,1,4,2,3,2,1]
countingSort(data)
print(data)