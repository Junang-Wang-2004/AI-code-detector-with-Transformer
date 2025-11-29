class Solution:
    def sumOddLengthSubarrays(self, arr):
        length = len(arr)
        answer = 0
        for pos in range(length):
            ways_left = pos + 1
            ways_right = length - pos
            num_odd = (ways_left * ways_right + 1) // 2
            answer += arr[pos] * num_odd
        return answer
