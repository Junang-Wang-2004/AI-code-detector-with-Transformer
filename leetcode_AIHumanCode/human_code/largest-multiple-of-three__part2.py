# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def largestMultipleOfThree(self, digits):
        """
        """
        def candidates_gen(r):
            if r == 0:
                return
            for i in range(10):
                yield [i]
            for i in range(10):
                for j in range(i+1):
                    yield [i, j]

        count, r = collections.Counter(digits), sum(digits)%3
        for deletes in candidates_gen(r):
            delete_count = collections.Counter(deletes)
            if sum(deletes)%3 == r and \
               all(count[k] >= v for k, v in delete_count.items()):
                for k, v in delete_count.items():
                    count[k] -= v
                break
        result = "".join(str(d)*count[d] for d in reversed(range(10)))
        return "0" if result and result[0] == '0' else result
