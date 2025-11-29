class Solution:
    def countSubranges(self, nums1, nums2):
        MOD = 10**9 + 7
        answer = 0
        states = {}
        for p1, p2 in zip(nums1, nums2):
            next_states = {}
            next_states[p1] = next_states.get(p1, 0) + 1
            next_states[-p2] = next_states.get(-p2, 0) + 1
            for delta, cnt in states.items():
                nd1 = delta + p1
                next_states[nd1] = (next_states.get(nd1, 0) + cnt) % MOD
                nd2 = delta - p2
                next_states[nd2] = (next_states.get(nd2, 0) + cnt) % MOD
            states = next_states
            answer = (answer + states.get(0, 0)) % MOD
        return answer
