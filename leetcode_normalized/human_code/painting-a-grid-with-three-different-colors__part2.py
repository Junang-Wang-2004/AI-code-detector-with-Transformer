# Time:  O(n * 3^m)
# Space: O(3^m)
import collections


# better complexity for small m, large n
class Solution2(object):
    def colorTheGrid(self, m, n):
        """
        """
        MOD = 10**9+7
        def find_masks(m, basis):  # Time: 3 + 3*2 + 3*2*2 + ... + 3*2^(m-1) = 3 * (2^m - 1) = O(2^m), Space: O(2^m)
            masks = [0]
            for c in range(m):
                new_masks = []
                for mask in masks:
                    choices = {0, 1, 2}
                    if c > 0:
                        choices.discard(mask//basis)  # get left grid
                    for x in choices:
                        new_masks.append((x*basis)+(mask//3))  # encoding mask
                masks = new_masks
            return masks

        def find_adj(m, basis, dp):
