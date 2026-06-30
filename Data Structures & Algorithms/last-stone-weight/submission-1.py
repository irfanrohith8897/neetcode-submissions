import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp=[]
        heapq.heapify(temp)
        for stone in stones:
            heapq.heappush(temp,-stone)

        while len(temp)>1:
            a=-heapq.heappop(temp)
            b=-heapq.heappop(temp)
            print(a,b,-abs(b-a))
            if a==b:
                continue
            else:
                heapq.heappush(temp,-abs(b-a))
        
        return -temp[0] if temp else 0
            

















