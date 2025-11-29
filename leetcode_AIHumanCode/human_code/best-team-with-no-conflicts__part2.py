# Time:  O(nlogs)
# Space: O(n)
# optimized from Solution4
class Solution2(object):
    def bestTeamScore(self, scores, ages):
        """
        """
        players = sorted(zip(ages, scores))
        sorted_scores = sorted(set(scores))
        lookup = {score:i for i, score in enumerate(sorted_scores)}  # coordinate compression
        segment_tree = SegmentTree(len(lookup))
        result = 0
        for age, score in players:
            segment_tree.update(lookup[score], lookup[score], segment_tree.query(0, lookup[score])+score)
        return segment_tree.query(0, len(lookup)-1)
 

