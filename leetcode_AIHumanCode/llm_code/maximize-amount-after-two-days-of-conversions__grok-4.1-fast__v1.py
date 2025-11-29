import collections

class Solution:
    def maxAmount(self, home, trades_a, multipliers_a, trades_b, multipliers_b):
        def setup_links(transactions, factors):
            connections = collections.defaultdict(list)
            for j in range(len(transactions)):
                x, y = transactions[j]
                ratio = factors[j]
                connections[x].append((y, ratio))
                connections[y].append((x, 1.0 / ratio))
            return connections

        def spread_values(values, links):
            to_process = list(values.keys())
            while to_process:
                next_to_process = []
                for node in to_process:
                    for target, gain in links[node]:
                        improved = values[node] * gain
                        if improved > values[target]:
                            values[target] = improved
                            next_to_process.append(target)
                to_process = next_to_process

        holdings_a = collections.defaultdict(float)
        holdings_a[home] = 1.0
        graph_a = setup_links(trades_a, multipliers_a)
        spread_values(holdings_a, graph_a)

        trades_b_rev = [[y, x] for x, y in trades_b]
        graph_b_rev = setup_links(trades_b_rev, multipliers_b)
        holdings_b_rev = collections.defaultdict(float)
        holdings_b_rev[home] = 1.0
        spread_values(holdings_b_rev, graph_b_rev)

        peak = 0.0
        for unit in holdings_a:
            peak = max(peak, holdings_a[unit] * holdings_b_rev[unit])
        return peak
