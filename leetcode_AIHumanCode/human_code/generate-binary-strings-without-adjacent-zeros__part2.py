# Time:  O(n * 2^n)
# Space: O(n * 2^n)
# bfs
class Solution2(object):
    def validStrings(self, n):
        """
        """
        q = [[]]
        for _ in range(n):
            new_q = []
            for x in q:
                if not x or x[-1] == '1':
                    new_q.append(x+['0'])
                new_q.append(x+['1'])
            q = new_q
        return ["".join(x) for x in q]
