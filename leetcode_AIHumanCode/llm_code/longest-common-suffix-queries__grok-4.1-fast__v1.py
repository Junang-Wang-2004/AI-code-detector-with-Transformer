class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        INF = float('inf')
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.minpair = (INF, INF)
        
        root = TrieNode()
        
        for idx, word in enumerate(wordsContainer):
            wlen = len(word)
            current = root
            current.minpair = min(current.minpair, (wlen, idx))
            for pos in range(wlen - 1, -1, -1):
                char = word[pos]
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
                current.minpair = min(current.minpair, (wlen, idx))
        
        result = []
        for query in wordsQuery:
            current = root
            qlen = len(query)
            for pos in range(qlen - 1, -1, -1):
                char = query[pos]
                if char not in current.children:
                    break
                current = current.children[char]
            _, bestidx = current.minpair
            result.append(int(bestidx))
        
        return result
