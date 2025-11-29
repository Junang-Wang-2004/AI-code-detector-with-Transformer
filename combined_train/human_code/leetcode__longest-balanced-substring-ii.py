import collections

class C1(object):

    def longestBalanced(self, a1):
        """
        """

        def count1():
            v1 = v2 = 0
            for v3 in range(len(a1)):
                v2 += 1
                if v3 + 1 == len(a1) or a1[v3 + 1] != a1[v3]:
                    v1 = max(v1, v2)
                    v2 = 0
            return v1

        def count2(a1, a2):
            v1 = v2 = 0
            v3 = collections.defaultdict(int, {v2: -1})
            for v4, v5 in enumerate(a1):
                if v5 == a1:
                    v2 += 1
                elif v5 == a2:
                    v2 -= 1
                else:
                    v2 = 0
                    v3 = collections.defaultdict(int, {v2: v4})
                    continue
                if v2 in v3:
                    v1 = max(v1, v4 - v3[v2])
                else:
                    v3[v2] = v4
            return v1

        def count3():
            v1 = v2 = v3 = 0
            v4 = collections.defaultdict(int, {(v2, v3): -1})
            for v5, v6 in enumerate(a1):
                if v6 == 'a':
                    v2 += 1
                elif v6 == 'b':
                    v3 += 1
                else:
                    v2 -= 1
                    v3 -= 1
                if (v2, v3) in v4:
                    v1 = max(v1, v5 - v4[v2, v3])
                else:
                    v4[v2, v3] = v5
            return v1
        return max(count1(), count2('a', 'b'), count2('b', 'c'), count2('c', 'a'), count3())
