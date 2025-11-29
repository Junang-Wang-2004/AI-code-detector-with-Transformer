import bisect
import itertools

MAXIMUM_LENGTH = 16
SPECIAL_NUMBERS = []

def compute_palindromes():
    palindromes = set()
    for m in range(1, 512):
        half = []
        center = None
        is_valid = True
        for j in range(9):
            if (m & (1 << j)) != 0:
                digit_val = j + 1
                repeat_count = digit_val // 2
                half += [str(digit_val)] * repeat_count
                if digit_val % 2 != 0:
                    if center is not None:
                        is_valid = False
                        break
                    center = str(digit_val)
        if not is_valid:
            continue
        half_length = len(half)
        pal_length = 2 * half_length + (1 if center else 0)
        if pal_length > MAXIMUM_LENGTH:
            continue
        for p in set(itertools.permutations(half)):
            left_side = ''.join(p)
            palindrome_str = left_side + (center or '') + left_side[::-1]
            palindromes.add(int(palindrome_str))
    global SPECIAL_NUMBERS
    SPECIAL_NUMBERS[:] = sorted(palindromes)

compute_palindromes()

class Solution(object):
    def specialPalindrome(self, n):
        pos = bisect.bisect_right(SPECIAL_NUMBERS, n)
        return SPECIAL_NUMBERS[pos]
