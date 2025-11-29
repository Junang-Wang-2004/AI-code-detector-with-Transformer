# Time:  O(l * nlogn)
# Space: O(1)

# sort
class Solution(object):
    def phonePrefix(self, numbers):
        """
        """
        numbers.sort()
        return all(not numbers[i+1].startswith(numbers[i]) for i in range(len(numbers)-1))


