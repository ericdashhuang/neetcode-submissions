class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        matches = 0
        for i in s1:
            count1[ord(i) - ord("a")] += 1

        for i in range(len(s1)):
            count2[ord(s2[i]) - ord("a")] += 1

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        l = 0

        if matches == 26: return True

        for r in range(len(s1), len(s2)):

            count2[ord(s2[r]) - ord("a")] += 1
            if count2[ord(s2[r])-ord("a")] == count1[ord(s2[r])-ord("a")]: 
                matches += 1
            elif count2[ord(s2[r])-ord("a")] == count1[ord(s2[r])-ord("a")] +1:
                matches -= 1

            count2[ord(s2[l]) - ord("a")] -= 1
            if count2[ord(s2[l])-ord("a")] == count1[ord(s2[l])-ord("a")]: matches += 1
            elif count2[ord(s2[l])-ord("a")] == count1[ord(s2[l])-ord("a")] - 1:
                matches -= 1
            l += 1
            
            if matches == 26: return True
        return False




