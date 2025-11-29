class Solution:
    def largestMultipleOfThree(self, digits):
        freq = [0] * 10
        total_sum = 0
        for num in digits:
            freq[num] += 1
            total_sum += num
        remainder = total_sum % 3
        if remainder != 0:
            adjusted = False
            # Attempt single digit removal
            for d in range(10):
                if freq[d] > 0 and d % 3 == remainder:
                    freq[d] -= 1
                    adjusted = True
                    break
            if not adjusted:
                # Attempt two digit removal
                for d1 in range(10):
                    if freq[d1] == 0:
                        continue
                    m1 = d1 % 3
                    needed = (remainder - m1) % 3
                    for d2 in range(10):
                        if d1 != d2 and freq[d2] == 0:
                            continue
                        m2 = d2 % 3
                        if m2 != needed:
                            continue
                        if d1 == d2:
                            if freq[d1] >= 2:
                                freq[d1] -= 2
                                adjusted = True
                                break
                        else:
                            freq[d1] -= 1
                            freq[d2] -= 1
                            adjusted = True
                            break
                    if adjusted:
                        break
        # Construct the largest number
        result = []
        for d in range(9, -1, -1):
            result.extend(str(d) * freq[d])
        s = ''.join(result)
        return "0" if not s or s[0] == '0' else s
