import collections

class Solution(object):
    def minExtraChar(self, s, dictionary):
        length = len(s)
        root = {}
        for term in dictionary:
            current = root
            for letter in term:
                if letter not in current:
                    current[letter] = {}
                current = current[letter]
            current['#'] = True
        LARGE = length + 1
        costs = [LARGE] * (length + 1)
        costs[0] = 0
        queue = collections.deque([0])
        while queue:
            start = queue.popleft()
            cost = costs[start]
            next_pos = start + 1
            if next_pos <= length and costs[next_pos] > cost + 1:
                costs[next_pos] = cost + 1
                queue.append(next_pos)
            current = root
            for pos in range(start, length):
                ch = s[pos]
                if ch not in current:
                    break
                current = current[ch]
                if '#' in current:
                    end = pos + 1
                    if costs[end] > cost:
                        costs[end] = cost
                        queue.appendleft(end)
        return costs[length]
