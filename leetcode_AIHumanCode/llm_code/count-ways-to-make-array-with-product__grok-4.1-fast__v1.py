class Solution(object):
    def waysToFillArray(self, queries):
        MOD = 10**9 + 7
        MAX_EXP = 100
        max_target = max(q[1] for q in queries)
        sieve_limit = int(max_target ** 0.5) + 2

        def generate_primes(limit):
            if limit < 2:
                return []
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(limit ** 0.5) + 1):
                if is_prime[i]:
                    for multiple in range(i * i, limit + 1, i):
                        is_prime[multiple] = False
            return [i for i in range(2, limit + 1) if is_prime[i]]

        prime_list = generate_primes(sieve_limit)

        def extract_exponents(number, primes_list):
            counts = []
            current = number
            for p in primes_list:
                if p * p > current:
                    break
                multiplicity = 0
                while current % p == 0:
                    current //= p
                    multiplicity += 1
                if multiplicity > 0:
                    counts.append(multiplicity)
            if current > 1:
                counts.append(1)
            return counts

        small_factorial = [1] * (MAX_EXP + 1)
        for idx in range(1, MAX_EXP + 1):
            small_factorial[idx] = small_factorial[idx - 1] * idx % MOD
        inv_factorials = [pow(small_factorial[i], MOD - 2, MOD) for i in range(MAX_EXP + 1)]

        def repeated_combination(types, repeats, modulus, invfacts):
            if repeats == 0:
                return 1
            accum = 1
            for offset in range(repeats):
                accum = accum * ((types + offset) % modulus) % modulus
            return accum * invfacts[repeats] % modulus

        outcomes = []
        for entry in queries:
            array_size, product_val = entry
            power_counts = extract_exponents(product_val, prime_list)
            result = 1
            for power in power_counts:
                result = result * repeated_combination(array_size, power, MOD, inv_factorials) % MOD
            outcomes.append(result)
        return outcomes
