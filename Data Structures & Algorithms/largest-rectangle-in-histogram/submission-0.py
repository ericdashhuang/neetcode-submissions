class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        res = float("-inf")
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                pi, ph = stack.pop()
                res = max(res, ph * (i - pi))
                start = pi
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res


