class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a

        total = len(a) + len(b)
        half = total//2

        l, r = 0, len(a) - 1
        while True:
            aidx = l + (r-l)//2
            bidx = half - aidx - 2

            aleft = a[aidx] if aidx >= 0 else float("-inf")
            aright = a[aidx + 1] if aidx + 1 < len(a) else float("inf")
            bleft = b[bidx] if bidx >= 0 else float("-inf")
            bright = b[bidx + 1] if bidx + 1 < len(b) else float("inf")

            if aleft <= bright and bleft <= aright:
                if total%2:
                    #odd
                    return min(aright, bright)
                else:
                    #even
                    return (max(aleft, bleft) + min(aright, bright))/2
            elif aleft > bright:
                r = aidx - 1
            else: 
                l = aidx + 1
