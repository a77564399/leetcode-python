# Python TR
# Time：2021/8/20 4:03 下午
# coding = utf-8
import collections
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hash = collections.Counter(words)
        print(hash)
        # res = sorted(hash,key=lambda word:(-hash[word],word))
        # print(sorted(hash, key=lambda word: (-hash[word], word)))
        print(sorted(hash, key=lambda i:len(i)))
        # return res[:k]
    if __name__ == '__main__':
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k=2
        topKFrequent(object,words,k)