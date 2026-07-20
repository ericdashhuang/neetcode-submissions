class TimeMap:

    def __init__(self):
        self.store = {} #key: [[value, timestamp]...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        resi = -1
        while l <= r:
            m = l + (r-l)//2
            time = values[m][1] 
            if time <= timestamp:
                resi = m
                l = m + 1
            elif time > timestamp: 
                r = m - 1
        return "" if resi == -1 else values[resi][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)