# Python TR
# Time：2021/8/18 7:36 下午
# coding = utf-8
class Solution(object):
    def findKthLargest(self,arr, k):
        k = len(arr)-k
        if not arr or k <= 0 or k > len(arr):
            return None
        index = self.partition(arr, 0, len(arr) - 1)
        while k - 1 != index:
            if k - 1 < index:
                index = self.partition(arr, 0, index - 1)
            else:
                index = self.partition(arr, index + 1, len(arr) - 1)
        return arr[k - 1]

    def partition(self,arr, low, high):
        key = arr[low]
        while low < high:
            while low < high and arr[high] >= key:
                high -= 1
            arr[low], arr[high] = arr[high], arr[low]
            while low < high and arr[low] <= key:
                low += 1
            arr[low], arr[high] = arr[high], arr[low]
        return low

x = Solution()
nums = [2,1]
k = len(nums)
print(x.findKthLargest(nums,2))
