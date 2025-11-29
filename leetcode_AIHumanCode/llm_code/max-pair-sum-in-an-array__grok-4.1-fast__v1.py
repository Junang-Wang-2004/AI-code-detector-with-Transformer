class Solution(object):
    def maxSum(self, nums):
        top1 = [-1] * 10
        top2 = [-1] * 10
        
        def largest_digit(val):
            if val == 0:
                return 0
            highest = 0
            while val > 0:
                highest = max(highest, val % 10)
                val //= 10
            return highest
        
        for num in nums:
            dig = largest_digit(num)
            if top1[dig] == -1 or num > top1[dig]:
                top2[dig] = top1[dig]
                top1[dig] = num
            elif top2[dig] == -1 or num > top2[dig]:
                top2[dig] = num
        
        answer = -1
        for i in range(10):
            if top2[i] != -1:
                answer = max(answer, top1[i] + top2[i])
        return answer
