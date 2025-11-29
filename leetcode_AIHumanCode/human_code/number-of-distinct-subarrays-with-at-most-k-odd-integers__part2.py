# Time:  O(n^2)
# Space: O(t), t is the size of trie
# suffix tree solution
class Solution2(object):
    def distinctSubarraysWithAtMostKOddIntegers(self, A, K):
        def countDistinct(A, left, right, trie):  # Time: O(n), Space: O(t)
            result = 0
            for i in range(left, right+1):
                if A[i] not in trie:
                    result += 1
                trie = trie[A[i]]
            return result

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        result = 0
        for left in range(len(A)):
            count = 0
            for right in range(left, len(A)):
                count += A[right]%2
                if count > K:
                    right -= 1
                    break
            result += countDistinct(A, left, right, trie)
        return result
