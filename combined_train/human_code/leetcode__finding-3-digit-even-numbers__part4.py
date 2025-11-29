import collections

class C1(object):

    def findEvenNumbers(self, a1):
        """
        """
        v1 = 3

        def backtracking(a1, a2, a3):
            if len(a1) == v1:
                a3.append(reduce(lambda x, y: x * 10 + y, a1))
                return
            for v1, (v2, v3) in enumerate(a2):
                if not a1 and v2 == 0 or (len(a1) == v1 - 1 and v2 % 2 != 0):
                    continue
                a2[v1][1] -= 1
                a2[v1], a2[-1] = (a2[-1], a2[v1])
                v4 = []
                if a2[-1][1] == 0:
                    v4 = a2.pop()
                a1.append(v2)
                backtracking(a1, a2, a3)
                a1.pop()
                if v4:
                    a2.append(v4)
                a2[v1], a2[-1] = (a2[-1], a2[v1])
                a2[v1][1] += 1
        v2 = collections.Counter(a1)
        v3 = list(map(list, iter(v2.items())))
        v4 = []
        backtracking([], v3, v4)
        v4.sort()
        return v4
