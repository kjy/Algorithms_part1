# Read file, parse, and put values in in list format
import urllib2
fileopen = urllib2.urlopen("https://d396qusza40orc.cloudfront.net/algo1%2Fprogramming_prob%2F2sum.txt")
line = fileopen.readlines()  # a list of 10,000 numbers in string format

uset = set()

for i in line:
    x = i.rstrip("\n")
    uset.add(int(x))

list1 = list(uset)

len(list1)   # 999752


##>>> list1[0]
##8399093760
##>>> list1[-1]
##61003355477

# Use mergeSort algorithm or something else

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

"""
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
"""
 # Or use built-in function 
list1.sort()


##>>> list1[0]
##-99999887310
##>>> list1[-1]
##99999662302



 def binary_search(L, v):
    """ (list, object) -> int

    Precondition: L is sorted from smallest to largest, and
    all the items in L can be compared to v.

    Return the index of the first occurrence of v in L, or
    return -1 if v is not in L.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    """

    b = 0
    e = len(L) - 1

    while b <= e:
        m = (b + e) // 2
        if L[m] < v:
            b = m + 1
        else:
            e = m - 1

    if b == len(L) or L[b] != v:
        return -1
    else:
        return b

    
    
counter=0
list2 = []
for t in range(-10000,10001):
    for x in list1:
        y = t-x
        if ((y in list1) & (x!=y)): 
            r=[x,y]
            r.sort()
            if r not in list2:
                list2.append(r)
                counter += 1

   
       












"""
list1 = [-10001,1,2,-10001]
expected result: 3 (got 6)

list1 = [-10001,1,2,-10001,9999]
expected result:5 (got 10)

list1 = [-7590801,-3823598,-5316263,-2616332,-7575597,-621530,-7469475,1084712,-7780489,-5425286,3971489,
-57444,1371995,-5401074,2383653,1752912,7455615,3060706,613097,-1073084,7759843,7267574,-7483155,-2935176,
-5128057,-7881398,-637647,-2607636,-3214997,-8253218,2980789,168608,3759759,-5639246,555129,-4489068,44019,
2275782,-3506307,-8031288,-213609,-4524262,-1502015,-1040324,3258235,32686,1047621,-3376656,7601567,-7051390
,6633993,-6245148,4994051,-4259178,856589,6047000,1785511,4449514,-1177519,4972172,8274315,7725694,-4923179,
5076288,-876369,-7663790,1613721,4472116,-4587501,3194726,6195357,-3364248,-113737,6260410,1974241,3174620,
3510171,7289166,4532581,-6650736,-3782721,7007010,6007081,-7661180,-1372125,-5967818,516909,-7625800,-2700089,
-7676790,-2991247,2283308,1614251,-4619234,2741749,567264,4190927,5307122,-5810503,-6665772]

expectd result: 6 (got 12)

For each list1, divide by 2 to get answer


In python I used a dictionary to hold the data.  The dictionary has about 100,000+ records
(much less than the million that we would get if we added each input record to
the dictionary).
Each key has a associated list of input values that fall in range of the key.
No key has more than 17 values.  I then work thru the dictionary looking at each value x.
I calculcate the range of values that could be added to x to  arrive at the necessary interval(- 10000 to 10000).
I can easily then locate the one or two records in the hashtable that would could contain that range.
I then look at the list associated with that key or keys. It runs very quickly and gives the correct answer.

to find the complement, you need to use a python set and then it goes quite quick.
It calculated everything for me in about 2 minutes.



""""




