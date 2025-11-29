class Solution(object):
    def maximumScore(self, nums, k):
        MOD = 10**9 + 7
        def generate_primes(limit):
            if limit < 2:
                return []
            flags = [True] * (limit + 1)
            flags[0] = flags[1] = False
            for i in range(2, int(limit ** 0.5) + 1):
                if flags[i]:
                    for j in range(i * i, limit + 1, i):
                        flags[j] = False
            return [i for i in range(limit + 1) if flags[i]]
        max_num = max(nums)
        sqrt_limit = int(max_num ** 0.5) + 1
        prime_list = generate_primes(sqrt_limit)
        prime_count_cache = {}
        def distinct_prime_count(number):
            if number in prime_count_cache:
                return prime_count_cache[number]
            temp = number
            distinct = 0
            for p in prime_list:
                if p * p > temp:
                    break
                if temp % p == 0:
                    distinct += 1
                    while temp % p == 0:
                        temp //= p
            if temp > 1:
                distinct += 1
            prime_count_cache[number] = distinct
            return distinct
        omega_list = [distinct_prime_count(x) for x in nums]
        length = len(nums)
        left_bounds = [-1] * length
        stack_left = [-1]
        for idx in range(length):
            while stack_left[-1] != -1 and omega_list[stack_left[-1]] < omega_list[idx]:
                stack_left.pop()
            left_bounds[idx] = stack_left[-1]
            stack_left.append(idx)
        right_bounds = [length] * length
        stack_right = [length]
        for idx in range(length - 1, -1, -1):
            while stack_right[-1] != length and omega_list[stack_right[-1]] <= omega_list[idx]:
                stack_right.pop()
            right_bounds[idx] = stack_right[-1]
            stack_right.append(idx)
        subarray_counts = []
        for idx in range(length):
            left_len = idx - left_bounds[idx]
            right_len = right_bounds[idx] - idx
            subarray_counts.append(left_len * right_len)
        choices = [(nums[idx], subarray_counts[idx]) for idx in range(length)]
        choices.sort(reverse=True)
        total = 1
        left_k = k
        for value, count in choices:
            if left_k <= 0:
                break
            taken = min(count, left_k)
            total = (total * pow(value, taken, MOD)) % MOD
            left_k -= taken
        return total
