#insertion sort using a for loop
def insertionSort(array):
    for i in range(1, len(array)):
    #previous number in the array
        previousnumber = i - 1
        insertednumber = array[i]
        while (array[previousnumber] > array[i] and previousnumber >= 0):
            #moves the inserted number back
            insertednumber = array[i-1]

print(insertionSort([1, 2, 3]))
