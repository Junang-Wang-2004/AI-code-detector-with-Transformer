class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        lefts = moves.count('L')
        rights = moves.count('R')
        blanks = len(moves) - lefts - rights
        diff = rights - lefts
        return abs(diff) + blanks
