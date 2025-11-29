# Time:  O(2 * (1 + (9/49) + (9/49)^2 + ...)) = O(2/(1-(9/49)) = O(2.45)
# Space: O(1)
class Solution2(object):
    def rand10(self):
        """
        """
        while True:
            x = (rand7()-1)*7 + (rand7()-1)
            if x < 40:
                return x%10 + 1

