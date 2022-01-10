# Python TR
# Time：2021/8/16 2:51 下午
# coding = utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numSet = set()
        for i in nums:
            numSet.add(i)
        if len(numSet)==len(nums):
            return False
        else:
            return True