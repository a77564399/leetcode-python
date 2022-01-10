# Python TR
# Time：2021/8/11 11:56 下午
# coding = utf-8
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j=0
        if nums is None:
            return None
        for i in range(len(nums)):
            if nums[i]!=val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j = j+1
        return j

    if __name__ == '__main__':
        nums = [3, 2, 2, 3]
        val = 3
        print(removeElement(object,nums,val))

