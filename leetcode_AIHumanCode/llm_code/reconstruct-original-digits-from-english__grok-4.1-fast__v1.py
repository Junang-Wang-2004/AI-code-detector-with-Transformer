class Solution:
    def originalDigits(self, s):
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        nums = [0] * 10
        nums[0] = freq[ord('z') - ord('a')]
        nums[2] = freq[ord('w') - ord('a')]
        nums[4] = freq[ord('u') - ord('a')]
        nums[6] = freq[ord('x') - ord('a')]
        nums[8] = freq[ord('g') - ord('a')]
        
        nums[1] = freq[ord('o') - ord('a')] - nums[0] - nums[2] - nums[4]
        nums[3] = freq[ord('t') - ord('a')] - nums[2]
        nums[5] = freq[ord('f') - ord('a')] - nums[4]
        nums[7] = freq[ord('s') - ord('a')] - nums[6]
        nums[9] = freq[ord('n') - ord('a')] - nums[1] - nums[7]
        
        output = []
        for d in range(10):
            output.extend(str(d) * nums[d])
        return ''.join(output)
