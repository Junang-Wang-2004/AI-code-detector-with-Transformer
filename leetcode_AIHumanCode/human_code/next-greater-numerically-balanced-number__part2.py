# Time:  O(l * c) = O(1), c is the count of all balanced's permutations, l is the max length of permutations
# Space: O(l * b) = O(1), b is the count of balanced
class Solution2(object):
    def nextBeautifulNumber(self, n):
        """
        """
        def next_permutation(nums, begin, end):
            def reverse(nums, begin, end):
                left, right = begin, end-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1

            k, l = begin-1, begin
            for i in reversed(range(begin, end-1)):
                if nums[i] < nums[i+1]:
                    k = i
                    break
            else:
                reverse(nums, begin, end)
                return False
            for i in reversed(range(k+1, end)):
                if nums[i] > nums[k]:
                    l = i
                    break
            nums[k], nums[l] = nums[l], nums[k]
            reverse(nums, k+1, end)
            return True

        # obtained by manually enumerating min number of permutations in each length
        balanced = [1,
                    22,
                    122, 333,
                    1333, 4444,
                    14444, 22333, 55555,
                    122333, 155555, 224444, 666666]
        s = list(str(n))
        result = 1224444
        for x in balanced:
            x = list(str(x))
            if len(x) < len(s):
                continue
            if len(x) > len(s):
                result = min(result, int("".join(x)))
                continue
            while True:
                if x > s:
                    result = min(result, int("".join(x)))
                if not next_permutation(x, 0, len(x)):  # distinct permutations
                    break
        return result


