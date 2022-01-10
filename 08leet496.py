# Python TR
# Time：2021/8/13 10:36 下午
# coding = utf-8
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        indexlist= []
        for data in nums1:
            flag = True
            idx = nums2.index(data)
            for i in range(idx,len(nums2)):
                if nums2[i]>data:
                    flag = False
                    indexlist.append(nums2[i])
                    break
            if flag:
                indexlist.append(-1)
        return indexlist

    if __name__ == '__main__':
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        print(nextGreaterElement(object,nums1,nums2))
