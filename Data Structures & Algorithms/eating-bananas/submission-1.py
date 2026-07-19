class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float("inf")
        while l <= r:
            m = l + (r-l)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            if time <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
