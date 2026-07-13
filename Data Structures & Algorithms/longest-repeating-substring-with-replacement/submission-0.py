class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            if sum(count.values()) - max(count.values()) <= k:
                
                res = max(r-l+1, res)
            else:
                count[s[l]] -= 1
                l += 1
                
        return res
            
            
