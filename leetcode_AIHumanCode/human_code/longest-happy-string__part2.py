# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def longestDiverseString(self, a, b, c):
        """
        """
        choices = [[a, 'a'], [b, 'b'], [c, 'c']]
        result = []
        for _ in range(a+b+c):
            choices.sort(reverse=True)
            for i, (x, c) in enumerate(choices):
                if x and result[-2:] != [c, c]:
                    result.append(c)
                    choices[i][0] -= 1
                    break
            else:
                break
        return "".join(result)
