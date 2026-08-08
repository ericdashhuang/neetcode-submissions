class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        nslow = 0
        while True:
            nslow = nums[nslow]
            slow = nums[slow]
            if nslow == slow:
                return nslow

        
