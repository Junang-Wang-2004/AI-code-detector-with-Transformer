import heapq

class C1:

    def minimizeStringValue(self, a1):
        v1 = [0] * 26
        v2 = 0
        for v3 in a1:
            if v3 == '?':
                v2 += 1
            else:
                v1[ord(v3) - ord('a')] += 1
        v4 = []
        for v5 in range(26):
            heapq.heappush(v4, (v1[v5], v5))
        v6 = [0] * 26
        for v7 in range(v2):
            v8, v9 = heapq.heappop(v4)
            v6[v9] += 1
            heapq.heappush(v4, (v8 + 1, v9))
        v10 = []
        for v5 in range(26):
            v10.extend([chr(ord('a') + v5)] * v6[v5])
        v11 = []
        v12 = 0
        for v3 in a1:
            if v3 == '?':
                v11.append(v10[v12])
                v12 += 1
            else:
                v11.append(v3)
        return ''.join(v11)
