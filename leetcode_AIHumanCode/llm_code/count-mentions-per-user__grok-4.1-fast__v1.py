class Solution(object):
    def countMentions(self, numberOfUsers, events):
        n = numberOfUsers
        counts = [0] * n
        next_online = [1] * n
        sorted_events = sorted(events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        for etype, tstr, content in sorted_events:
            t = int(tstr)
            if etype == "OFFLINE":
                next_online[int(content)] = t + 60
            elif content == "ALL":
                for i in range(n):
                    counts[i] += 1
            elif content == "HERE":
                for i in range(n):
                    if next_online[i] <= t:
                        counts[i] += 1
            else:
                for word in content.split():
                    uid = int(word[2:])
                    counts[uid] += 1
        return counts
