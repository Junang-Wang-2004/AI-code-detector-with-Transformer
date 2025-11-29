# Time:  O(n)
# Space: O(n)
# trie solution
class Trie(object):
    def __init__(self):
        self.__root = {}
        
    def insert(self, num):
        node = self.__root
        for i in reversed(range(32)):
            curr = (num>>i) & 1
            if curr not in node:
                node[curr] = {"_count":0}
            node = node[curr]
            node["_count"] += 1
                
    def query(self, num, limit):
        node, result = self.__root, 0
        for i in reversed(range(32)):
            curr = (num>>i) & 1
            bit = (limit>>i) & 1
            if bit:
                if curr in node:
                    result += node[0^curr]["_count"]  # current limit is xxxxx1*****, count xor pair with xxxxx0***** pattern
            if bit^curr not in node:
                break
            node = node[bit^curr]
        return result


class Solution2(object):
    def countPairs(self, nums, low, high):
        """
        """
        result = 0
        trie = Trie()
        for x in nums:
            result += trie.query(x, high+1)-trie.query(x, low)
            trie.insert(x)
        return result
