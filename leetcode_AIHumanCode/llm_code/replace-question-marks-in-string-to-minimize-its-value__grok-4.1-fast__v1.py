import heapq

class Solution:
    def minimizeStringValue(self, s):
        counts = [0] * 26
        num_q = 0
        for ch in s:
            if ch == '?':
                num_q += 1
            else:
                counts[ord(ch) - ord('a')] += 1
        pq = []
        for i in range(26):
            heapq.heappush(pq, (counts[i], i))
        deltas = [0] * 26
        for _ in range(num_q):
            cf, idx = heapq.heappop(pq)
            deltas[idx] += 1
            heapq.heappush(pq, (cf + 1, idx))
        fillers = []
        for i in range(26):
            fillers.extend([chr(ord('a') + i)] * deltas[i])
        output = []
        pos = 0
        for ch in s:
            if ch == '?':
                output.append(fillers[pos])
                pos += 1
            else:
                output.append(ch)
        return ''.join(output)
