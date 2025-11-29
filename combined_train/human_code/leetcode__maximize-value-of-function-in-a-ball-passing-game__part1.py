import collections

class C1(object):

    def getMaxFunctionValue(self, a1, a2):
        """
        """

        def find_cycles(a1):
            v1 = []
            v2 = [0] * len(a1)
            v3 = 0
            for v4 in range(len(a1)):
                v5 = v3
                while not v2[v4]:
                    v3 += 1
                    v2[v4] = v3
                    v4 = a1[v4]
                if v2[v4] > v5:
                    v1.append((v4, v3 - v2[v4] + 1))
            return v1

        def find_prefixes():
            v1 = [(-1, -1)] * len(a1)
            v2 = [[0] for v3 in range(len(cycles))]
            for v4, (v5, v6) in enumerate(cycles):
                for v7 in range(v6):
                    v1[v5] = (v4, v7)
                    v2[v4].append(v2[v4][v7] + v5)
                    v5 = a1[v5]
            return (v1, v2)

        def get_sum(a1, a2, a3):
            v1 = len(a1) - 1
            v2, v3 = divmod(a3, v1)
            return v2 * a1[-1] + (a1[min(a2 + v3, v1)] - a1[a2]) + (a1[max((a2 + v3 - v1, 0))] - a1[0])

        def start_inside_cycle():
            v1 = 0
            for v2, v3 in cycles:
                for v4 in range(v3):
                    v5, v6 = lookup[v2]
                    v1 = max(v1, get_sum(prefixes[v5], v6, a2 + 1))
                    v2 = a1[v2]
            return v1

        def start_outside_cycle():
            v1 = 0
            v2 = [0] * len(a1)
            for v3 in a1:
                v2[v3] += 1
            for v4 in range(len(a1)):
                if v2[v4]:
                    continue
                v5 = 0
                v6 = collections.deque()
                while lookup[v4][0] == -1:
                    v5 += v4
                    v6.append(v4)
                    if len(v6) == a2 + 1:
                        v1 = max(v1, v5)
                        v5 -= v6.popleft()
                    v4 = a1[v4]
                v7, v8 = lookup[v4]
                while v6:
                    v1 = max(v1, v5 + get_sum(prefixes[v7], v8, a2 + 1 - len(v6)))
                    v5 -= v6.popleft()
            return v1
        v1 = find_cycles(a1)
        v2, v3 = find_prefixes()
        return max(start_inside_cycle(), start_outside_cycle())
