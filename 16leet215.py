# Python TR
# Time：2021/8/18 4:42 下午
# coding = utf-8
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums==None or len(nums)==0:
            return None
        for i in len(nums):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        return -res