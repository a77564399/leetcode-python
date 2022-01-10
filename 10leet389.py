# Python TR
# Time：2021/8/16 9:52 上午
# coding = utf-8
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s)==0:
            return t
        dict = {}
        for i,char in enumerate(s):
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] = dict[char] + 1
        for char in t:
            if char not in dict:
                return char
            dict[char] = dict[char] - 1
        for char in t:
            if dict[char]==-1:
                return char

    if __name__ == '__main__':
        s = "a"
        t = "aa"
        print(findTheDifference(object,s,t))