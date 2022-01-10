# Python TR
# Time：2021/8/20 1:24 下午
# coding = utf-8
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dict = {}
        lenList = []
        res = []
        findLen = len(words)-k
        for i,word in enumerate(words):
            dict[len(word)] = i
            lenList.append(len(word))
        self.quickSore(lenList,0,len(lenList)-1,findLen)
        for i in range(findLen,len(lenList)):
            res.append(words[dict[lenList[i]]])
        return res
    def quickSore(self,nums,low,high,findLen):
        idx = self.partition(nums, low, high)
        if idx<findLen:
            self.quickSore(nums,idx+1,high)
        else:
            self.quickSore(nums,low,idx-1)
            self.quickSore(nums,idx+1,high)


    def partition(self,nums,low,high):
        if nums==None or len(nums)==0:
            return None
        temp = nums[low]
        while low<high:
            while low<high and temp<nums[high]:
                high-=1
            nums[high] = nums[low]
            while low<high and nums[low]<temp:
                low+=1
            nums[low] = nums[high]
        nums[low] = temp
        return low

    if __name__ == '__main__':
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k=2
        topKFrequent(object,words,k)


