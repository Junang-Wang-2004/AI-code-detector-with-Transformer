# Time:  O(n^2 + w * l)
# Space: O(t)
import itertools


# trie, dp
class Solution3(object):
    def minimumCost(self, target, words, costs):
        """
        """
        INF = float("inf")
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__mns = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                self.__mns.append(INF)
                return len(self.__nodes)-1

            def add(self, w, c):
                curr = 0
                for x in w:
                    x = ord(x)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
                self.__mns[curr] = min(self.__mns[curr], c)
            
            def query(self, i):
                curr = 0
                for j in range(i, len(target)):
                    x = ord(target[j])-ord('a')
                    if self.__nodes[curr][x] == -1:
                        break
                    curr = self.__nodes[curr][x]
                    if self.__mns[curr] != INF:
                        dp[j+1] = min(dp[j+1], dp[i]+self.__mns[curr])
    
        trie = Trie()
        for w, c in zip(words, costs):
            trie.add(w, c)
        dp = [INF]*(len(target)+1)
        dp[0] = 0
        for i in range(len(target)):
            if dp[i] == INF:
                continue
            trie.query(i)
        return dp[-1] if dp[-1] != INF else -1
