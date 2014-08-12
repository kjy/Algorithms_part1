


counter = 0
def partition(myList, left, right): #left and right are the start and end indixes of the subarray
    #Make the counter global so that it will increment up and the quicksort function can return it
    global counter
    #Make swap between first and last element to make the pivot the last element
    myList[left],myList[right]=myList[right],myList[left]
    pivot = myList[left] # choose first element in subarray as pivot
    # i is the boundary for what we have looked at already and separates what is less than, greater than pivot
    i = left+1
    # j is the boundary for what we have looked at and what we have not looked at
    j = left+1   
    
    for j in range(left+1, right + 1):
        counter += 1
        if myList[j] < pivot:          # if myList[j] > pivot, then do nothing
   
            myList[j],myList[i]= myList[i], myList[j] # do the swap
            i += 1
            
   
            
    myList[left],myList[i-1]=myList[i-1],myList[left] # swap where pivot needs to be

    position = i-1 # Keep track of location of pivot by index

   
    return position #new pivot position. Used to divide the next left and right side of the array.
   
            




def quicksort(myList, left, right):
    #global tally 
    if left < right:# this is enough to end recursion
        pivot_pos = partition(myList, left, right)
        x = len(myList[left:pivot_pos-1])
        y = len(myList[pivot_pos+1:right])
                    
 #       tally = tally + (x-1)
                   
#        tally = tally + (y-1)

        quicksort(myList, left, pivot_pos - 1)
        quicksort(myList, pivot_pos + 1, right)



        
    return myList,counter
           
        
        
        

"""
for size 10 array, first = 25, last = 29, median = 21
>>> blist = [3,9,8,4,6,10,2,5,7,1]
>>> quicksort(blist,0,9)
([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25)



for size 100 array, first = 615 last = 587, median = 518
>>> clist = [57, 97, 17, 31, 54, 98, 87, 27, 89, 81, 18, 70, 3, 34, 63, 100, 46, 30, 99,
         10, 33, 65, 96, 38, 48, 80, 95, 6, 16, 19, 56, 61, 1, 47, 12, 73, 49, 41, 37,
         40, 59, 67, 93, 26, 75, 44, 58, 66, 8, 55, 94, 74, 83, 7, 15, 86, 42, 50, 5, 22,
         90, 13, 69, 53, 43, 24, 92, 51, 23, 39, 78, 85, 4, 25, 52, 36, 60, 68, 9, 64, 79,
         14, 45, 2, 77, 84, 11, 71, 35, 72, 28, 76, 82, 88, 32, 21, 20, 91, 62, 29]
>>> quicksort(clist,0,99)
([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71,
72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
95, 96, 97, 98, 99, 100], 615)



first = 31, last = 35, median = 24
>>> dlist = [2,5,4,3,0,9,8,6,1,20,17]
>>> quicksort(dlist,0,10)
([0, 1, 2, 3, 4, 5, 6, 8, 9, 17, 20], 31)


"""
