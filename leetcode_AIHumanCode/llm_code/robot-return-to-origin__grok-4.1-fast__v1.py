class Solution(object):
    def judgeCircle(self, moves):
        horiz = moves.count('R') - moves.count('L')
        vert = moves.count('U') - moves.count('D')
        return horiz == 0 and vert == 0
