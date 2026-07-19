class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #list[row#][column#]
        
        l = 0
        r = len(matrix)*len(matrix[0]) - 1
        while l <= r:
            m = l + (r-l)//2
            num = matrix[m//len(matrix[0])][m%len(matrix[0])]
            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return True
        return False
