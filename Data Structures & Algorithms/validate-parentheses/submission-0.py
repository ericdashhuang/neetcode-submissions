class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        pairs = {")": "(", "}": "{", "]": "["}
        for _ in s:
            if _ in "([{":
                res.append(_)
            else:
                if not res or pairs[_] != res[-1]:
                    return False
                res.pop()
        return len(res) == 0
      