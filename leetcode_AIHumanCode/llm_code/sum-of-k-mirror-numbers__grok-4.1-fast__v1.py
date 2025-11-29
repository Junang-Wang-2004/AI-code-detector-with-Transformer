class Solution:
    def kMirror(self, k, n):
        def generate_pal_base_k(b):
            digs = [1]
            while True:
                yield digs[:]
                ln = len(digs)
                p = ln // 2
                while p < ln:
                    if digs[p] < b - 1:
                        digs[p] += 1
                        digs[ln - 1 - p] = digs[p]
                        break
                    digs[p] = 0
                    digs[ln - 1 - p] = 0
                    p += 1
                else:
                    digs.insert(0, 1)
                    digs[-1] = 1

        def decimal_value(dlist, base):
            val = 0
            for digit in dlist:
                val = val * base + digit
            return val

        def is_decimal_palindrome(num):
            reversed_num = 0
            temp = num
            while temp > 0:
                reversed_num = reversed_num * 10 + temp % 10
                temp //= 10
            return reversed_num == num

        pal_gen = generate_pal_base_k(k)
        total_sum = 0
        found = 0
        while found < n:
            current_digs = next(pal_gen)
            current_num = decimal_value(current_digs, k)
            if is_decimal_palindrome(current_num):
                total_sum += current_num
                found += 1
        return total_sum
