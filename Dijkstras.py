import urllib2
fileopen1 = urllib2.urlopen("http://spark-public.s3.amazonaws.com/algo1/programming_prob/dijkstraData.txt")
line2 = fileopen1.readlines()

graph = {}
for u in range(len(line)):
    x = line[u].split("\t")
    x.pop(-1)
    len(x) #28
    key1 = x[0]
    list1 = []
    for i in range(1,len(x)):
        list1 = list1 + x[i].split(",")

    numbers = [ int(x) for x in list1]                       
    listEven = numbers[::2] # Even index (will be keys)
    listOdd = numbers[1::2] # Odd index  (will be values)

    Even = [str(x) for x in listEven]


    graph[key1]={key:value for (key,value) in zip(Even,listOdd)}

    
import sys

def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxint)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

if __name__ == "__main__":
    graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}
    print shortestpath(graph,'a','b')

    """
    graph = {'a': {'w': 14, 'x': 7, 'y': 9},
            'b': {'w': 9, 'z': 6},
            'w': {'a': 14, 'b': 9, 'y': 2},
            'x': {'a': 7, 'y': 10, 'z': 15},
            'y': {'a': 9, 'w': 2, 'x': 10, 'z': 11},
            'z': {'b': 6, 'x': 15, 'y': 11}}

    Result:
        (20, ['a', 'y', 'w', 'b'])



"""


    
