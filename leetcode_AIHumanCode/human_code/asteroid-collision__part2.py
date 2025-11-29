# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def asteroidCollision(self, asteroids):
        """
        """
        result = []
        for x in asteroids:
            while result and x < 0 < result[-1]:
                if result[-1] < -x:
                    result.pop()
                    continue
                elif result[-1] == -x:
                    result.pop()
                break
            else:
                result.append(x)
        return result
