class Solution:
    def longestSubsequenceRepeatedK(self, s, k):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        ans = []
        def feasible(pattern, txt, reps):
            if not pattern:
                return True
            ptr = 0
            found = 0
            for char in txt:
                if char == pattern[ptr]:
                    ptr += 1
                    if ptr == len(pattern):
                        found += 1
                        ptr = 0
                        if found == reps:
                            return True
            return False
        def explore(curr_path, curr_freq):
            if not feasible(curr_path, s, k):
                return
            if len(curr_path) > len(ans):
                ans[:] = curr_path[:]
            for oc in range(ord('z'), ord('a') - 1, -1):
                ch = chr(oc)
                if curr_freq.get(ch, 0) >= k:
                    curr_freq[ch] = curr_freq.get(ch, 0) - k
                    curr_path.append(ch)
                    explore(curr_path, curr_freq)
                    curr_path.pop()
                    curr_freq[ch] += k
        explore([], freq)
        return "".join(ans)
