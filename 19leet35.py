# Python TR
# Time：2021/9/13 8:30 下午
# coding = utf-8
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return mid
        return l