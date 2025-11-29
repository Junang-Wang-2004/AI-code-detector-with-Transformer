import math
import cmath

def fft_transform(arr, is_inverse):
    length = len(arr)
    if length <= 1:
        return
    num_bits = (length - 1).bit_length()
    for idx in range(length):
        rev_idx = 0
        temp = idx
        for _ in range(num_bits):
            rev_idx = (rev_idx << 1) | (temp & 1)
            temp >>= 1
        if idx < rev_idx:
            arr[idx], arr[rev_idx] = arr[rev_idx], arr[idx]
    step_size = 2
    while step_size <= length:
        theta = 2 * math.pi / step_size * (-1 if is_inverse else 1)
        omega_step = complex(math.cos(theta), math.sin(theta))
        for start in range(0, length, step_size):
            omega = complex(1, 0)
            half = step_size // 2
            for k in range(half):
                idx1 = start + k
                idx2 = idx1 + half
                u_val = arr[idx1]
                v_val = arr[idx2] * omega
                arr[idx1] = u_val + v_val
                arr[idx2] = u_val - v_val
                omega *= omega_step
        step_size *= 2
    if is_inverse:
        scale = 1.0 / length
        for i in range(length):
            arr[i] *= scale

def polynomial_multiply(p, q):
    target_size = len(p) + len(q) - 1
    fft_size = 1
    while fft_size < target_size:
        fft_size <<= 1
    padded_p = [complex(coef, 0) for coef in p] + [0j] * (fft_size - len(p))
    padded_q = [complex(coef, 0) for coef in q] + [0j] * (fft_size - len(q))
    fft_transform(padded_p, False)
    fft_transform(padded_q, False)
    for pos in range(fft_size):
        padded_p[pos] *= padded_q[pos]
    fft_transform(padded_p, True)
    return [int(round(c.real)) for c in padded_p[:target_size]]

class Solution(object):
    def multiply(self, poly1, poly2):
        return polynomial_multiply(poly1, poly2)
