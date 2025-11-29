class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        balance = 0
        lowest = 0
        low_idx = -1
        overall = 0
        for i in range(n):
            delta = gas[i] - cost[i]
            overall += delta
            balance += delta
            if balance < lowest:
                lowest = balance
                low_idx = i
        if overall < 0:
            return -1
        return (low_idx + 1) % n
