class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force
        res = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                res = max(res, (r-l)*(min(heights[l], heights[r])))
        return res