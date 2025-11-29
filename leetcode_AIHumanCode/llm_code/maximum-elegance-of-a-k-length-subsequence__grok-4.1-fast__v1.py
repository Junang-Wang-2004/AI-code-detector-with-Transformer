class Solution:
    def findMaximumElegance(self, items, k):
        sorted_items = sorted(items, key=lambda x: -x[0])
        n = len(sorted_items)
        total = 0
        used_colors = set()
        replacements = []
        for i in range(min(k, n)):
            p, c = sorted_items[i]
            total += p
            if c in used_colors:
                replacements.append(p)
            used_colors.add(c)
        num_distinct = len(used_colors)
        max_elegance = total + num_distinct * num_distinct
        color_max = {}
        for i in range(k, n):
            p, c = sorted_items[i]
            if c not in used_colors:
                color_max[c] = max(color_max.get(c, 0), p)
        new_prices = sorted(color_max.values(), reverse=True)
        replacements.sort()
        curr_total = total
        num_repls = min(len(replacements), len(new_prices))
        for i in range(num_repls):
            curr_total += new_prices[i] - replacements[i]
            curr_distinct = num_distinct + i + 1
            max_elegance = max(max_elegance, curr_total + curr_distinct * curr_distinct)
        return max_elegance
