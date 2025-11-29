class Solution:
    def numDifferentIntegers(self, word):
        unique_nums = set()
        idx = 0
        n = len(word)
        while idx < n:
            if word[idx].isdigit():
                val = 0
                while idx < n and word[idx].isdigit():
                    val = val * 10 + int(word[idx])
                    idx += 1
                unique_nums.add(val)
            else:
                idx += 1
        return len(unique_nums)
