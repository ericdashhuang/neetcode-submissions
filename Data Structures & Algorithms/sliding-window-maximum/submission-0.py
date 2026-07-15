class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for r in range(len(nums)):
            if dq:
                if dq[0] < r-k+1:
                    dq.popleft()
            
           
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            res.append(nums[dq[0]])
        del res[:k-1]
        return res

           