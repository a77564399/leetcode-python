# Python TR
# Time：2021/8/12 10:55 上午
# coding = utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

    if __name__ == '__main__':
        nums = [3, 2, 2, 3]
        val = 3
        print(removeElement(object,nums,val))