class TimeMap:

    def __init__(self):
        self.store = {} # hashmap (mapstore)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        res = ""

        # binary search on values 
        lo = 0
        hi = len(values) - 1

        while lo <= hi:
            mid = (lo + hi) //2
            mid_timestamp = values[mid][1]

            if mid_timestamp <= timestamp:
                res = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return res
