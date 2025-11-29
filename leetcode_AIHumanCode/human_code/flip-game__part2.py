# Time:  O(c * m * n + n) = O(c * n + n), where m = 2 in this question
# Space: O(n)
# This solution compares O(m) = O(2) times for two consecutive "+", where m is length of the pattern
class Solution2(object):
  def generatePossibleNextMoves(self, s):
      """
      """
      return [s[:i] + "--" + s[i+2:] for i in range(len(s) - 1) if s[i:i+2] == "++"]


