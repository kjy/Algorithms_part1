import urllib2
fileopen = urllib2.urlopen("http://spark-public.s3.amazonaws.com/algo1/programming_prob/IntegerArray.txt")
line = fileopen.readlines()

temp = []
for i in range(len(line)):
    l = line[i].split("\r\n")
    l.remove(l[1])
    temp.append(int(l[0]))

fileopen.close()
len(temp)
beforelist = temp[:]
len(beforelist)

def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
   
    #print("Merging ",alist)

#alist = [54,26,93,17,77,31,44,55,20]
#mergeSort(alist)
#print(alist)

mergeSort(temp)


            
def countinversions(a,b):
    
    counter = 0
    while a !=[]:
        part = 0
        val = a[0]
        indval = b.index(val)
        if a[0]==b[0]:
            a.pop(0)
            b.pop(indval)
           
        else:
            counter = counter + indval
            a.pop(0)
            b.pop(indval)
    
    print(counter)


countinversions(temp,beforelist)
#2407905288 number of inversions

"""
Test cases:

a = [1,2,3,4,5,6]
b= [1, 2, 3, 4, 5, 6]
answer = 0

a = [1,3,5,2,4,6]
b = [1, 2, 3, 4, 5, 6]
answer = 3


a = [5,4,3,2,1]
b = [1, 2, 3, 4, 5]
answer = 10


a = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
answer = 56


a = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16,
     48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42,
     12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15,
     36, 20, 8, 9, 49, 22, 23, 30, 45]
     
b = b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
         16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
         29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
         43, 44, 45, 46, 47, 48, 49]
         
answer=590

a = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8,
     49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67,
     14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63,
     97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75,
     58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34,
     65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
     22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
     42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,
     62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
     82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

answer= 2372


"""
