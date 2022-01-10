# Python TR
# Time：2021/8/15 11:29 下午
# coding = utf-8
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        flag = False
        for i,num in enumerate(nums):
            if num in dict:
                flag = True
                break
            dict[num] = i
        return flag

    if __name__ == '__main__':
        nums = [1,2,3,4]
        print(containsDuplicate(object,nums))
