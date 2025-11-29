class Solution(object):
    def countPairs(self, deliciousness):
        MOD = 10**9 + 7
        max_val = max(deliciousness)
        powers_of_two = []
        power = 1
        while power <= 2 * max_val:
            powers_of_two.append(power)
            power *= 2
        frequency = {}
        total = 0
        for num in deliciousness:
            for pow_two in powers_of_two:
                needed = pow_two - num
                total = (total + frequency.get(needed, 0)) % MOD
            frequency[num] = frequency.get(num, 0) + 1
        return total
