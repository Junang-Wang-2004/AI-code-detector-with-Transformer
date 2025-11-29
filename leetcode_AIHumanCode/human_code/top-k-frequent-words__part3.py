# Time:  O(n + klogk) ~ O(n + nlogn)
# Space: O(n)
# Bucket Sort Solution
class Solution3(object):
    def topKFrequent(self, words, k):
        """
        """
        counts = collections.Counter(words)
        buckets = [[] for _ in range(len(words)+1)]
        for word, count in counts.items():
            buckets[count].append(word)
        pairs = []
        for i in reversed(range(len(words))):
            for word in buckets[i]:
                pairs.append((-i, word))
            if len(pairs) >= k:
                break
        pairs.sort()
        return [pair[1] for pair in pairs[:k]]


# time: O(nlogn)
# space: O(n)

from collections import Counter


class Solution4(object):
    def topKFrequent(self, words, k):
        """
        """
        counter = Counter(words)
        candidates = list(counter.keys())
        candidates.sort(key=lambda w: (-counter[w], w))
        return candidates[:k]
