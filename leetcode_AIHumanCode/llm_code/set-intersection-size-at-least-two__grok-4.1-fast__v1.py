class Solution(object):
    def intersectionSizeTwo(self, segments):
        segments.sort(key=lambda t: (-t[0], t[1]))
        m = len(segments)
        demands = [2] * m
        answer = 0
        for pos in range(m):
            left, right = segments[pos]
            places = demands[pos]
            answer += places
            for mark in range(left, left + places):
                for nxt in range(pos + 1, m):
                    if demands[nxt] and mark <= segments[nxt][1]:
                        demands[nxt] -= 1
        return answer
