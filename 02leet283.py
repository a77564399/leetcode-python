# Python TR
# Time：2021/8/11 9:26 下午
# coding = utf-8
class Solution(object):
    def moveZeroes(self, nums):
        zeroList = []
        zeroidx = []
        for i,num in enumerate(nums):
            if num == 0:
                zeroidx.append(i)
                zeroList.append(0)
        for idx in zeroidx:
            del nums[idx]
        for num in zeroList:
            nums.append(num)
        return nums

    if __name__ == '__main__':
        nums = [0,0,1]
        print(moveZeroes(object,nums))
