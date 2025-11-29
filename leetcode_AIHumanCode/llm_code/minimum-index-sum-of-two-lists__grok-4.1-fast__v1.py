class Solution:
    def findRestaurant(self, list1, list2):
        indices1 = {}
        for position, dish in enumerate(list1):
            indices1[dish] = position
        
        min_total = float('inf')
        for position, dish in enumerate(list2):
            if dish in indices1:
                total = indices1[dish] + position
                if total < min_total:
                    min_total = total
        
        matches = []
        for position, dish in enumerate(list2):
            if position > min_total:
                break
            if dish in indices1 and indices1[dish] + position == min_total:
                matches.append(dish)
        return matches
