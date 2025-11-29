class Solution(object):
    def isSelfCrossing(self, dist):
        n = len(dist)
        if n < 4:
            return False
        a = dist[0]
        b = dist[1]
        c = dist[2]
        d = dist[3]
        if d >= b and a >= c:
            return True
        if n == 4:
            return False
        e = dist[4]
        if e >= c and b >= d:
            return True
        if b == d and a + e >= c:
            return True
        i = 5
        while i < n:
            f = dist[i]
            if f >= d and c >= e:
                return True
            if b <= d and f + b >= d and e <= c and a + e >= c:
                return True
            a = b
            b = c
            c = d
            d = e
            e = f
            i += 1
        return False
