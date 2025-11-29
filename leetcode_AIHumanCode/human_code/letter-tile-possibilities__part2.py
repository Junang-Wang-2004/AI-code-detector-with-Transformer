# Time:  O(r), r is the value of result
# Space: O(n)
class Solution2(object):
    def numTilePossibilities(self, tiles):
        """
        """
        def backtracking(counter):
            total = 0
            for k, v in counter.items():
                if not v:
                    continue
                counter[k] -= 1
                total += 1+backtracking(counter)
                counter[k] += 1
            return total

        return backtracking(collections.Counter(tiles))
