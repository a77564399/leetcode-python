# Python TR
# Time：2021/9/13 9:29 下午

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return -1
        l = 0
        r = len(nums)-1
        while l<r:
            m = l + int((r-l)/2)
            if nums[m]<nums[m+1]:
                l = m+1
            else:
                r = m
        return r

s = Solution()
nums = [1,2,3,1]
print(s.findPeakElement(nums))