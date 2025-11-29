# Time:  O(n + logc), c is the number of candies
# Space: O(1)
class Solution2(object):
    def distributeCandies(self, candies, num_people):
        """
        """
        # find max integer p s.t. sum(1 + 2 + ... + p) <= C
        left, right = 1, candies
        while left <= right:
            mid = left + (right-left)//2
            if not ((mid <= candies*2 // (mid+1))):
                right = mid-1
            else:
                left = mid+1
        p = right
        remaining = candies - (p+1)*p//2
        rows, cols = divmod(p, num_people)
        
        result = [0]*num_people
        for i in range(num_people):
            result[i] = (i+1)*(rows+1) + (rows*(rows+1)//2)*num_people if i < cols else \
                        (i+1)*rows + ((rows-1)*rows//2)*num_people
        result[cols] += remaining
        return result


