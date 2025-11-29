# Time:  O(nlogn)
# Space: O(n)

# sort, line sweep
class Solution(object):
    def separateSquares(self, squares):
        """
        """
        events = []
        for x, y, l in squares:
            events.append((y, 1, l))
            events.append((y+l, -1, l))
        events.sort(key=lambda e: e[0])
        total = curr = 0.0
        prev = events[0][0]
        for y, v, l in events:
            if y != prev:
                total += (y-prev)*curr
                prev = y
            curr += l*v
        expect = total/2.0
        total = curr = 0.0
        prev = events[0][0]
        for y, v, l in events:
            if y != prev:
                if total+(y-prev)*curr >= expect:
                    break
                total += (y-prev)*curr
                prev = y
            curr += l*v
        return prev+(expect-total)/curr


