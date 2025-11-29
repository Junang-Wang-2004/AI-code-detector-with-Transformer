# Time:  O(n * l)
# Space: O(t)
# trie
class Solution_TLE(object):
    def longestCommonPrefix(self, words, k):
        """
        """
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__cnt = []
                self.__mx = []
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                self.__cnt.append(0)
                self.__mx.append(0)
                return len(self.__nodes)-1

            def update(self, w, d, k):
                path = [-1]*(len(w)+1)
                path[0] = curr = 0
                for i, c in enumerate(w, 1):
                    x = ord(c)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    path[i] = curr = self.__nodes[curr][x]
                for i in reversed(range(len(path))):
                    curr = path[i]
                    self.__cnt[curr] += d
                    self.__mx[curr] = i if self.__cnt[curr] >= k else 0
                    for x in range(len(self.__nodes[curr])):
                        if self.__nodes[curr][x] != -1:
                            self.__mx[curr]= max(self.__mx[curr], self.__mx[self.__nodes[curr][x]])

            def query(self):
                return self.__mx[0]
        

        result = [0]*len(words)
        trie = Trie()
        for w in words:
            trie.update(w, +1, k)
        for i in range(len(words)):
            trie.update(words[i], -1, k)
            result[i] = trie.query()
            trie.update(words[i], +1, k)
        return result
