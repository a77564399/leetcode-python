# Python TR
# Time：2021/9/19 2:38 下午
# coding = utf-8

import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)==0:
            return False
        matrix = np.array(matrix).flatten().tolist()
        l = 0
        r = len(matrix)-1
        while l<=r:
            mid = l + int((r-l)/2)
            if matrix[mid]==target:
                return True
            elif matrix[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return False



s = Solution()
nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(nums,13))
