# Python TR
# Time：2021/8/11 11:47 下午
# coding = utf-8
class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i,num in enumerate(nums):
            if nums[i]!=0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j = j+1
        return nums

    if __name__ == '__main__':
        nums = [0,0,1]
        print(moveZeroes(object,nums))