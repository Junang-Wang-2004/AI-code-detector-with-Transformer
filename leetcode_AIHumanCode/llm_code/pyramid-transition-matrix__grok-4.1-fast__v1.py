class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        trans = {}
        for rule in allowed:
            p = (rule[0], rule[1])
            trans.setdefault(p, []).append(rule[2])
        memo = {}

        def feasible(pyr):
            if len(pyr) == 1:
                return True
            if pyr in memo:
                return memo[pyr]
            width = len(pyr) - 1
            stack = ['?'] * width

            def extend(col):
                if col == width:
                    return feasible(''.join(stack))
                pair = pyr[col:col + 2]
                for opt in trans.get(pair, []):
                    stack[col] = opt
                    if extend(col + 1):
                        return True
                return False

            outcome = extend(0)
            memo[pyr] = outcome
            return outcome

        return feasible(bottom)
