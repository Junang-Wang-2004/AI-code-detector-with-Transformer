class Solution:
    def fixedRatio(self, s, num1, num2):
        balance_count = {0: 1}
        answer = 0
        balance = 0
        for ch in s:
            if ch == '1':
                balance += num1
            else:
                balance -= num2
            answer += balance_count.get(balance, 0)
            if balance in balance_count:
                balance_count[balance] += 1
            else:
                balance_count[balance] = 1
        return answer
