# Time:  O(w * l + n * l)
# Space: O(n + t), t is the total size of trie
# trie, dp
class Solution4(object):
    def minValidStrings(self, words, target):
        """
        """
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                return len(self.__nodes)-1

            def add(self, w):
                curr = 0
                for c in w:
                    x = ord(c)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
            
            def query(self, target, i):
                curr = 0
                for l in range(len(target)-i):
                    x = ord(target[i+l])-ord('a')
                    if self.__nodes[curr][x] == -1:
                        return l
                    curr = self.__nodes[curr][x]
                return len(target)-i

        trie = Trie()
        for w in words:
            trie.add(w)
        lookup = [0]*len(target)
        for i in range(len(target)):
            l = trie.query(target, i)
            for nl in range(1, l+1):
                lookup[i+nl-1] = max(lookup[i+nl-1], nl)
        dp = [0]*(len(target)+1)
        for i in range(len(target)):
            if not lookup[i]:
                return -1
            dp[i+1] = dp[(i-lookup[i])+1]+1
        return dp[-1]
