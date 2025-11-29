class Solution:
    def mostPopularCreator(self, creators, ids, views):
        sums = {}
        maxima = {}
        for creator, video, count in zip(creators, ids, views):
            sums[creator] = sums.get(creator, 0) + count
            if creator not in maxima or count > maxima[creator][0]:
                maxima[creator] = (count, video)
            elif count == maxima[creator][0]:
                maxima[creator] = (count, min(video, maxima[creator][1]))
        highest = max(sums.values())
        output = []
        for creator in sums:
            if sums[creator] == highest:
                output.append([creator, maxima[creator][1]])
        return output
