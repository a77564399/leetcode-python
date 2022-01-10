# Python TR
# Time：2021/8/18 7:36 下午
# coding = utf-8
class Solution(object):
    def getIndex(self,nums,low,high):
        temp = nums[low]
        while low<high:
            while low<high and temp<=nums[high]:
                high = high-1
            nums[low] = nums[high]
            while low<high and nums[low]<=temp:
                low = low + 1
            nums[high] = nums[low]

        nums[low] = temp
        return low
    def quickSearch(self,nums,low,high,k):
        if low<=high:
            idx = self.getIndex(nums,low,high)
            if idx == k:
                # nums = nums[low:]
                # print(nums[k])
                return nums[k] #排好这个位置后k是恒定不变的，所以要输出的是数组k元素
            elif idx<k:
                # print(1)
                return self.quickSearch(nums,idx+1,high,k)
            else:
                return self.quickSearch(nums,low,idx-1,k)
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        res_idx = len(nums)-k

        return self.quickSearch(nums,low,high,res_idx)

x = Solution()
nums = [2,1]
k = len(nums)
print(x.findKthLargest(nums,2))
