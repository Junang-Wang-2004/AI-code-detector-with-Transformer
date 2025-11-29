# Time:  O(10^6), the most times of finding x is 665502 (k = 7, n = 30)
# Space: O(1)
class Solution2(object):
    def kMirror(self, k, n):
        """
        """
        def num_gen(k):
            digits = ['0']
            while True:
                for i in range(len(digits)//2, len(digits)): 
                    if int(digits[i])+1 < k:
                        digits[i] = digits[-1-i] = str(int(digits[i])+1)
                        break
                    digits[i] = digits[-1-i] = '0'
                else:
                    digits.insert(0, '1')
                    digits[-1] = '1'
                yield "".join(digits)
        
        def mirror_num(gen):
            while True:
                x = int(next(gen, k), k)
                if str(x) == str(x)[::-1]:
                    break
            return x

        gen = num_gen(k)
        return sum(mirror_num(gen) for _ in range(n))
