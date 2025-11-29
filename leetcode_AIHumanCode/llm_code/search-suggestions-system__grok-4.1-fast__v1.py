import bisect

class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res = []
        current_prefix = ""
        for ch in searchWord:
            current_prefix += ch
            lower = bisect.bisect_left(products, current_prefix)
            next_prefix = current_prefix[:-1] + chr(ord(ch) + 1)
            upper = bisect.bisect_left(products, next_prefix)
            res.append(products[lower:min(lower + 3, upper)])
        return res
