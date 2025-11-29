class Solution:
    def maximumUnits(self, box_list, capacity):
        box_list.sort(key=lambda pair: -pair[1])
        total = 0
        idx = 0
        num_types = len(box_list)
        while capacity > 0 and idx < num_types:
            count, value = box_list[idx]
            if capacity >= count:
                total += count * value
                capacity -= count
            else:
                total += capacity * value
                capacity = 0
            idx += 1
        return total
