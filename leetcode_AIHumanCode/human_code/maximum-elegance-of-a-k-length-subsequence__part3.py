# Time:  O(nlogn)
# Space: O(k)
# sort, greedy
class Solution3(object):
    def findMaximumElegance(self, items, k):
        """
        """
        items.sort(reverse=True)
        result = curr = 0
        lookup = set()
        stk = []
        for i in range(k):
            if items[i][1] in lookup:
                stk.append(items[i][0])
            curr += items[i][0]
            lookup.add(items[i][1])
        result = curr+len(lookup)**2
        for i in range(k, len(items)):
            if items[i][1] in lookup:
                continue
            if not stk:
                break
            curr += items[i][0]-stk.pop()
            lookup.add(items[i][1])
            result = max(result, curr+len(lookup)**2)
        return result
