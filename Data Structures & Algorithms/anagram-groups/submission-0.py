class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for char in str:
                count [ord(char)-ord('a')] += 1
            hash[tuple(count)].append(str)
        return list(hash.values())