class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt = defaultdict(int)
        counts = defaultdict(int)
        res = ""
        resl = float("inf")
        for _ in t:
            countt[_] += 1
        
        l = 0
        have = 0
        want = len(countt)
        for r in range(len(s)):
            if s[r] in countt:
                counts[s[r]] += 1
                if countt[s[r]] == counts[s[r]]:
                    have += 1
            while have == want:
                if r-l+1 < resl:
                    resl = min(resl, r-l+1)
                    res = s[l:r+1]
                if s[l] in countt:
                    counts[s[l]] -= 1
                    if counts[s[l]] == countt[s[l]] - 1:
                        have -= 1
                l += 1
        return res
