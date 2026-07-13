class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}
        l = 0
        maxlength = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
                
            seen[s[r]] = r
            maxlength = max(maxlength, r-l+1)

        return maxlength

