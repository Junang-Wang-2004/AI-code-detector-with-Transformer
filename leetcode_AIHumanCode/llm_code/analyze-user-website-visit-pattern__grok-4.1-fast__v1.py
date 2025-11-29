class Solution:
    def mostVisitedPattern(self, usernames, timestamps, webs):
        user_sessions = {}
        n = len(usernames)
        for i in range(n):
            u = usernames[i]
            if u not in user_sessions:
                user_sessions[u] = []
            user_sessions[u].append((timestamps[i], webs[i]))
        pattern_freq = {}
        for session in user_sessions.values():
            session.sort(key=lambda x: x[0])
            sites = [site for _, site in session]
            m = len(sites)
            unique_patterns = set()
            for i in range(m):
                for j in range(i + 1, m):
                    for k in range(j + 1, m):
                        pat = (sites[i], sites[j], sites[k])
                        unique_patterns.add(pat)
            for pat in unique_patterns:
                pattern_freq[pat] = pattern_freq.get(pat, 0) + 1
        max_freq = -1
        result = None
        for pat, f in pattern_freq.items():
            if f > max_freq or (f == max_freq and (result is None or pat < result)):
                max_freq = f
                result = pat
        return list(result)
