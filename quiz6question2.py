# Read file, parse, and put values in in list format
import urllib2
fileopen = urllib2.urlopen("http://spark-public.s3.amazonaws.com/algo1/programming_prob/Median.txt")
line1 = fileopen.readlines()


list1 = []
for i in line1:
    x = i.rstrip("\n")
    list1.append(int(x))
  

len(list1) #10000
list1[0]
list1[-1]


list3 = []
list2 = []
for i in list1:
    list2.append(i)
    list2.sort()
    
    if len(list2)%2==0:  # if even
        ind = (len(list2)-1)/2
        medianvalue = list2[ind]
        list3.append(medianvalue)            
    else:                # if odd
        ind =(len(list2))/2
        medianvalue = list2[ind]
        list3.append(medianvalue)
  
       


result = sum(list3)%10000
    


"""
>>> list1 = [3,7,4,1,2,6,5]
(3,3,4,3,3,3,4) are medians
>>> result
23

list1 = [10,1,9,2,8,3,7,4,6,5]
>>> result
55

list1 = [4,5,6,7,8,9,10,1,2,3,4,8,9,14,-4]
>>> result
82

list1 = from object fileopen above, 10,000 integers
result
1213

"""
