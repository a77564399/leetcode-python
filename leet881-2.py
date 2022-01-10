# Python TR
# Time：2021/9/6 2:25 下午
# coding = utf-8
class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people)-1
        res = 0
        while(i<=j):
            if people[i]+people[j]<=limit:
                i+=1
            j-=1
            res+=1
        return res