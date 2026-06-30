from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxfreq=max(count.values())
        maxCount=sum(1 for i in count.values() if i==maxfreq)
        time=(maxfreq-1)*(n+1)+maxCount
        return time if time>len(tasks) else len(tasks)