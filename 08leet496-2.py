# Python TR
# Time：2021/8/13 11:55 下午
# coding = utf-8
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dict = {}
        Stack = []
        idxList = []
        for i,data in enumerate(nums2):
            while len(Stack)>0 and data>Stack[-1]:
                dict[Stack.pop()] = data
            Stack.append(data)
        for x in nums1:
            idxList.append(dict.setdefault(x,-1))
        return idxList

    if __name__ == '__main__':
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        print(nextGreaterElement(object, nums1, nums2))

