class Solution(object):
    def findRLEArray(self, encoded1, encoded2):
        ita = iter(encoded1)
        itb = iter(encoded2)
        output = []
        group_a = next(ita, None)
        group_b = next(itb, None)
        while group_a is not None and group_b is not None:
            val_a, rem_a = group_a
            val_b, rem_b = group_b
            step = min(rem_a, rem_b)
            product = val_a * val_b
            if output and output[-1][0] == product:
                output[-1][1] += step
            else:
                output.append([product, step])
            rem_a -= step
            rem_b -= step
            if rem_a == 0:
                group_a = next(ita, None)
            if rem_b == 0:
                group_b = next(itb, None)
        return output
