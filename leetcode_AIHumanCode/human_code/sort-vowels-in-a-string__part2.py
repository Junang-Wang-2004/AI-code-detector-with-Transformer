# Time:  O(nlogn)
# Space: O(1)
# sort
class Solution2(object):
    def sortVowels(self, s):
        """
        """
        VOWELS = "AEIOUaeiou"
        LOOKUP = set(VOWELS)
        vowels = [x for x in s if x in LOOKUP]
        vowels.sort(reverse=True)
        return "".join(vowels.pop() if x in LOOKUP else x for x in s)
