# Python TR
# Time：2021/8/11 10:12 下午
# coding = utf-8
#冒泡排序想法--错误
class Solution(object):
    def moveZeroes(self, nums):
        for num,i in enumerate(nums):
            if num == 0:
                for j in range(i,(len(nums)-1)):
                    nums[j] = nums[j+1]
                    nums[j+1] = 0
        return nums
    if __name__ == '__main__':
        nums = [0,1,0,3,12]
        print(moveZeroes(object,nums))