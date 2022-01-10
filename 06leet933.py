# Python TR
# Time：2021/8/13 8:32 下午
# coding = utf-8
from collections import deque


class RecentCounter(object):

    def __init__(self):
        self.count = 0
        self.queue = deque()

    def ping(self, t):
        self.queue.append(t)
        lastTime = t-3000
        while self.queue[0]<lastTime:
            self.queue.popleft()
        return len(self.queue)


counter = RecentCounter()
print(counter.ping(1))
print(counter.ping(100))