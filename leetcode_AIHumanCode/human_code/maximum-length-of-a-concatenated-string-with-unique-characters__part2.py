# Time:  O(2^n)
# Space: O(1)
class Solution2(object):
    def maxLength(self, arr):
        """
        """ 
        def bitset(s):
            result = 0
            for c in s:
                if result & power[ord(c)-ord('a')]:
                    return 0
                result |= power[ord(c)-ord('a')]
            return result
    
        bitsets = [bitset(x) for x in arr]
        result = 0
        for i in range(power[len(arr)]):
            curr_bitset, curr_len = 0, 0
            while i:
                j = i & -i  # rightmost bit
                i ^= j
                j = log2[j]  # log2(j)
                if not bitsets[j] or (curr_bitset & bitsets[j]):
                    break
                curr_bitset |= bitsets[j]
                curr_len += len(arr[j])
            else:
                result = max(result, curr_len)
        return result
