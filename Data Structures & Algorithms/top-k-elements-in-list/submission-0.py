class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num]=freq.get(num,0) + 1
        arr = []
        for num, cnt in freq.items():
            arr.append([cnt, num])
            arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
            

        