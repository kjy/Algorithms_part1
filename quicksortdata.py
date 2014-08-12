
import urllib2
fileopen = urllib2.urlopen("http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt")
line = fileopen.readlines()

array1 = []
for i in range(len(line)):
    l = line[i].split("\r\n")
    l.remove(l[1])
    array1.append(int(l[0]))

fileopen.close()

len(array1)
array1[0]
