class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = {}

        for i in s1:
            count1[i] = 1 + count1.get(i, 0)
        
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            count2 = {}
            for i in range(l, r+1):
                count2[s2[i]] = 1 + count2.get(s2[i], 0)
            if count2 == count1:
                return True
            l += 1
            r += 1
        return False
