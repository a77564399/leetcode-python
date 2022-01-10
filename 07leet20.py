# Python TR
# Time：2021/8/13 9:19 下午
# coding = utf-8
class Solution(object):
    def isValid(self, s):
        if len(s)==0:
            return True
        signList = list(s)
        Stack = []
        dict = {")":"(","}":"{","]":"["}
        for sign in signList:
            if len(Stack)==0:
                Stack.append(sign)
            elif sign=='(' or  sign=='{' or sign=='[':
                Stack.append(sign)
            elif dict[sign] == Stack[-1]:
                Stack.pop()

            else:
                Stack.append(sign)
        if len(Stack)==0:
            return True
        else:
            return False

    if __name__ == '__main__':
        s = "{[]}"
        print(isValid(object,s))