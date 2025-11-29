# Time:  ctor: O(n * l * log(n * l)), n is the number of products
#                                   , l is the average length of product name
#        suggest: O(l^2 * n)
# Space: O(n * l)
import bisect


class Solution3(object):
    def suggestedProducts(self, products, searchWord):
        """
        """
        products.sort()  # Time: O(n * l * log(n * l))
        result = []
        prefix = ""
        for i, c in enumerate(searchWord):  # Time: O(l)
            prefix += c
            start = bisect.bisect_left(products, prefix)  # Time: O(log(n * l))
            new_products = []
            for j in range(start, len(products)):  # Time: O(n * l)
                if not (i < len(products[j]) and products[j][i] == c):
                    break
                new_products.append(products[j])
            products = new_products
            result.append(products[:3])
        return result
