class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        block = set(forbidden)
        max_f = max(forbidden) if forbidden else 0
        limit = max(x, max_f) + a + 2 * b
        seen = set()
        frontier = [(0, True)]
        seen.add((0, True))
        jumps = 0
        while frontier:
            next_frontier = []
            for position, allow_back in frontier:
                if position == x:
                    return jumps
                # Try forward jump
                fwd_pos = position + a
                if fwd_pos <= limit and fwd_pos not in block:
                    fwd_state = (fwd_pos, True)
                    if fwd_state not in seen:
                        seen.add(fwd_state)
                        next_frontier.append(fwd_state)
                # Try backward jump if allowed
                if allow_back:
                    bwd_pos = position - b
                    if bwd_pos >= 0 and bwd_pos not in block:
                        bwd_state = (bwd_pos, False)
                        if bwd_state not in seen:
                            seen.add(bwd_state)
                            next_frontier.append(bwd_state)
            frontier = next_frontier
            jumps += 1
        return -1
