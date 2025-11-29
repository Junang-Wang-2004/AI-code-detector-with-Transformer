class Solution:
    def maxCompatibilitySum(self, students, mentors):
        rows = len(students)
        cols = len(mentors)
        qs = len(students[0])
        matches = []
        for s in students:
            r = []
            for t in mentors:
                agree = sum(1 for x, y in zip(s, t) if x == y)
                r.append(agree)
            matches.append(r)
        states = 1 << cols
        memo = [-1] * states
        memo[0] = 0
        for idx in range(rows):
            fresh = [-1] * states
            for state in range(states):
                if memo[state] == -1:
                    continue
                fresh[state] = max(fresh[state], memo[state])
                for pos in range(cols):
                    if (state & (1 << pos)) == 0:
                        next_state = state | (1 << pos)
                        score = memo[state] + matches[idx][pos]
                        fresh[next_state] = max(fresh[next_state], score)
            memo = fresh
        result = 0
        for val in memo:
            if val > result:
                result = val
        return result
