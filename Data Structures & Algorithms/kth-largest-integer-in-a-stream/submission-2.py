import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        heapq.heapify(self.nums)
        self.k=k
        while k<len(self.nums):
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        else:
            if self.nums[0]<val:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums,val)
        return self.nums[0]
