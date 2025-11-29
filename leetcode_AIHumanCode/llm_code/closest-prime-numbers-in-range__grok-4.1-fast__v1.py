import bisect

def generate_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

ALL_PRIMES = generate_primes(10**6)
NUM_GAPS = len(ALL_PRIMES) - 1
DIFFERENCES = [ALL_PRIMES[k + 1] - ALL_PRIMES[k] for k in range(NUM_GAPS)]

LOG_SIZE = 17
SPARSE_TABLE = [[0] * NUM_GAPS for _ in range(LOG_SIZE)]

for idx in range(NUM_GAPS):
    SPARSE_TABLE[0][idx] = idx

for level in range(1, LOG_SIZE):
    for pos in range(NUM_GAPS - (1 << level) + 1):
        cand1 = SPARSE_TABLE[level - 1][pos]
        cand2 = SPARSE_TABLE[level - 1][pos + (1 << (level - 1))]
        SPARSE_TABLE[level][pos] = cand1 if DIFFERENCES[cand1] <= DIFFERENCES[cand2] else cand2

def range_min_position(left_gap, right_gap):
    span = right_gap - left_gap + 1
    lg = span.bit_length() - 1
    pos1 = SPARSE_TABLE[lg][left_gap]
    pos2 = SPARSE_TABLE[lg][right_gap - (1 << lg) + 1]
    return pos1 if DIFFERENCES[pos1] <= DIFFERENCES[pos2] else pos2

class Solution(object):
    def closestPrimes(self, start_val, end_val):
        lo_idx = bisect.bisect_left(ALL_PRIMES, start_val)
        hi_idx = bisect.bisect_right(ALL_PRIMES, end_val) - 1
        if lo_idx >= hi_idx:
            return [-1, -1]
        gap_lo = lo_idx
        gap_hi = hi_idx - 1
        if gap_lo > gap_hi:
            return [-1, -1]
        best_pos = range_min_position(gap_lo, gap_hi)
        return [ALL_PRIMES[best_pos], ALL_PRIMES[best_pos + 1]]
