def insertionSort(array):    
    print(f"SORTING {array}")
    for i in range(1, len(array)):
        #previous index in the array     
        previousindex = i - 1
        currentvalue = array[i]
        currentindex = i
        while (array[currentindex - 1] > currentvalue and (currentindex - 1) >= 0):
            #swaps the inserted number with the number before it
            previousnumber = array[currentindex - 1]
            array[currentindex - 1] = currentvalue
            array[currentindex] = previousnumber
            currentindex -= 1   
    return array
        

print(insertionSort([1, 3, 2]))

print(insertionSort([1, 2, 3]))

print(insertionSort([6, 5, 4, 3, 2, 1]))

print(insertionSort([3, 2, 1, 5]))

print(insertionSort([2, 3, 1]))
