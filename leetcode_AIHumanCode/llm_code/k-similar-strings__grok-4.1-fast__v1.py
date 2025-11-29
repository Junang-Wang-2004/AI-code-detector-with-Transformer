import collections

class Solution:
    def kSimilarity(self, A, B):
        distance = {}
        queue = collections.deque([A])
        distance[A] = 0
        n = len(A)
        while queue:
            current = queue.popleft()
            if current == B:
                return distance[current]
            char_list = list(current)
            mismatch = 0
            while mismatch < n and char_list[mismatch] == B[mismatch]:
                mismatch += 1
            target_char = B[mismatch]
            for k in range(mismatch + 1, n):
                if char_list[k] == target_char:
                    char_list[mismatch], char_list[k] = char_list[k], char_list[mismatch]
                    next_state = ''.join(char_list)
                    if next_state not in distance:
                        distance[next_state] = distance[current] + 1
                        queue.append(next_state)
                    char_list[mismatch], char_list[k] = char_list[k], char_list[mismatch]
