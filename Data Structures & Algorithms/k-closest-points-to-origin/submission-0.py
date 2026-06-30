import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(x,y):
            d=math.sqrt(x**2+y**2)
            return d
        temp=[]
        heapq.heapify(temp)
        for l in points:
            dis=findDistance(l[0],l[1])
            heapq.heappush(temp,(-dis,l))
        while len(temp)>k:
            heapq.heappop(temp)

        return [i[1] for i in temp]