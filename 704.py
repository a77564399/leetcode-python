# Python TR
# Time：2021/9/8 7:11 下午
# coding = utf-8
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return -1
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        return -1
