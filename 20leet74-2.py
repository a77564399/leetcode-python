# Python TR
# Time：2021/9/19 3:23 下午
# coding = utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)==0:
            return False
        w = len(matrix[0])
        h = len(matrix)
        row = 0
        col = w-1
        # while row<h-1 and col>=0:
        while row<h-1 and matrix[row][col]<target:
            row+=1
        while col>=0 and matrix[row][col]>target:
            col-=1
        if matrix[row][col]==target:
            return True
        return False

s = Solution()
nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(s.searchMatrix(nums,13))