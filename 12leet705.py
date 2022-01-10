# Python TR
# Time：2021/8/17 8:53 上午
# coding = utf-8
class MyHashSet(object):

    def __init__(self):
        self.list = []

    def add(self, key):
        flag = True
        for num in self.list:
            if num == key:
                flag=False
        if flag:
            self.list.append(key)



    def remove(self, key):
        for idx,num in enumerate(self.list):
            if num==key:
                del self.list[idx]
                break



    def contains(self, key):
        for num in self.list:
            if num == key:
                return True
        return False

myHashSet = MyHashSet()
myHashSet.add(1)

