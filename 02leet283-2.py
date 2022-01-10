# Python TR
# Time：2021/8/11 10:39 下午
# coding = utf-8
class Solution(object):
    def moveZeroes(self, nums):
        i=0
        j=0
        while(i<len(nums)):
            if nums[i]==0:
                i = i+1
            else:
                temp = nums[j]
                nums[j]=nums[i]
                nums[i]=temp
                j = j+1 #注意1
                i = i+1
        return nums
    if __name__ == '__main__':
        nums = [1]
        print(moveZeroes(object,nums))
