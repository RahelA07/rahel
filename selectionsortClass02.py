
#Making an array for the sorting of the selection
array = [1, 2, 3, 4, 5, 7]

#Creating a functional header
def selectionSort(array):

#Creating a global variable then set it with the given leangth of the array
    n = len(array)

#Creating a for loop
    for i in range(n): #<--- whatever the length of the array is how many times you are going to run the loop

#Initially assume the first element of the unsorted 

        minimum = i
        
        #For loop
        for j in range(i+1, n):
        
        #Creating a comparison value , testing if j is less than the index (minimum) .
            if(array[j] < array[minimum]):

        #If it is, set it equal with j

                 minimum = j

        #Swap the minimum element with the first element unsorted part

        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp

    #return the array

    return array

 #print the selection sort

print(selectionSort(array))