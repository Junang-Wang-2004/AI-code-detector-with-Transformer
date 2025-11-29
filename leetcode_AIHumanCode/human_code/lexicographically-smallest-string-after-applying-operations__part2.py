# Time:  O(100 * n^2), at most O(100n) strings and each compare costs O(n)
# Space: O(n^2)
import collections


class Solution2(object):
    def findLexSmallestString(self, s, a, b):
        """
        """
        q, lookup, result = collections.deque([s]), {s}, s
        while q:
            curr = q.popleft()
            if curr < result:
                result = curr
            add_a = list(curr)    
            for i, c in enumerate(add_a):
                if i%2:
                    add_a[i] = str((int(c)+a) % 10)
            add_a = "".join(add_a)        
            if add_a not in lookup:
                lookup.add(add_a)
                q.append(add_a)
            rotate_b = curr[b:] + curr[:b]
            if rotate_b not in lookup:
                lookup.add(rotate_b)
                q.append(rotate_b)
        return result
