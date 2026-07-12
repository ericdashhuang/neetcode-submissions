class Solution:
    def trap(self, height: List[int]) -> int:

#         # #brute 
#         # if not height:
#         #     return 0
        
#         # res = 0

#         # for i in range(len(height)):
#         #     lmax = rmax = 0
#         #     for j in range(i):
#         #         lmax = max(height[j], lmax)
#         #     for k in range(i+1, len(height)):
#         #         rmax = max(height[k], rmax)
            
#         #     res += max(0, min(rmax, lmax) - height[i])
#         # return res
        
#         #prefix suffix array

        # if not height:
        #     return 0
        
        # res = 0

        # prefix = [0] * len(height)
        # suffix = [0] * len(height)

        # for i in range(1,len(height)):
        #     prefix[i] = max(prefix[i-1], height[i])
        # for i in range(len(height)-2, -1, -1):
        #     suffix[i] = max(suffix[i+1], height[i])
        
        # for i in range(len(height)):
        #     res += max(0, min(prefix[i], suffix[i]) - height[i])
        # return res

        #2pointer
        if not height:
            return 0 
        res = 0 
        l, r, = 0, len(height)-1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax<rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += max(0,min(lmax, rmax) - height[l])

            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += max(0, min(lmax, rmax) - height[r])
        return res


            

