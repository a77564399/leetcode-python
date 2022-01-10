# Python TR
# Time：2021/8/10 9:00 下午
# coding = utf-8
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=0
        r=0
        res = 0
        while(r<len(nums)):
            if nums[r]==1:
                r = r + 1
                res = max(res,r-l)
            else:
                r = r + 1
                l=r
        return res
    if __name__ == '__main__':
        nums = [1,1,1]
        print(findMaxConsecutiveOnes(object,nums))