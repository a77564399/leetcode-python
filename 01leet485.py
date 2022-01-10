# Python TR
# Time：2021/8/10 8:44 下午
# coding = utf-8
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        zero_num = 0
        max_num = 0
        for i in range(len(nums)):
            if nums[i]==1:
                zero_num = zero_num+1
                max_num = max(max_num,zero_num)
            else:
                max_num = max(max_num,zero_num)
                zero_num = 0
        return max_num

    if __name__ == '__main__':
        nums = [1,1,0,1,1,1]
        print(findMaxConsecutiveOnes(object,nums))
