# Time:  O((logn)^2)
# Space: O((logn)^2)
class Solution2(object):
    def minDays(self, n):
        result = 0
        q, lookup = [n], set([n])
        while q:
            new_q = []
            for i in q: 
                if not i:
                    return result
                if i-1 not in lookup:
                    lookup.add(i-1)
                    new_q.append(i-1)
                if i%2 == 0 and i//2 not in lookup:
                    lookup.add(i//2)
                    new_q.append(i//2)
                if i%3 == 0 and i//3 not in lookup:
                    lookup.add(i//3)
                    new_q.append(i//3)
            result += 1
            q = new_q
        return result
