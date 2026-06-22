class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []

        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        arr=self.d.get(key)
        print(type(arr))
        l=0
        r=len(arr)-1
        ans=""
        while l<=r:
            m=(l+r)//2
            if arr[m][1] <= timestamp:
                ans = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return ans