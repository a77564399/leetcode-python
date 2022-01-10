# Python TR
# Time：2021/8/27 9:12 上午
# coding = utf-8
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        if len(people)==1:
            return 1
        num = 0
        peopleList = sorted(people)
        i=0
        # for i in range(0,len(people),2):
        while i<len(peopleList):
            if i==len(peopleList)-1:
                num+=1
                break
            if peopleList[i]+peopleList[i+1]<=limit:
                num+=1
                i+=2
            else:
                break
        if i<len(peopleList)-1:
            num += len(peopleList)-i
        return num

    people = [5,1,4,2]
    print(numRescueBoats(object,people,6))