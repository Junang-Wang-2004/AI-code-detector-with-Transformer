from functools import reduce
# Time:  O(n)
# Space: O(n)
# string
class Solution2(object):
    def discountPrices(self, sentence, discount):
        """
        """
        def format(discount, x):
            return "${:d}.{:02d}".format(*divmod(int(x[1:])*(100-discount), 100)) if x[0] == '$' and x[1:].isdigit() else x

        return " ".join(format(discount, x) for x in sentence.split())
