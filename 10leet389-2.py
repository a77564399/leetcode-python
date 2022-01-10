# Python TR
# Time：2021/8/16 11:33 上午
# coding = utf-8
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_sum = 0
        s_sum = 0
        for char in t:
            t_sum = t_sum + ord(char)
        for char in s:
            s_sum = s_sum + ord(char)
        return chr(t_sum-s_sum)

    if __name__ == '__main__':
        s = "a"
        t = "aa"
        print(findTheDifference(object,s,t))