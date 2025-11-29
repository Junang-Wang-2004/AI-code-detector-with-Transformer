class C1(object):

    def maximumScore(self, a1, a2):
        """
        """

        def best_time_to_buy_and_sell_stock_v(a1):
            v1 = [0] * (len(a1) + 1)
            v2 = 0
            for v3 in range(a2):
                v4, v5 = (float('-inf'), float('-inf'))
                v6 = [float('-inf')] * (len(a1) + 1)
                for v7 in range(v3, len(a1)):
                    v4, v5 = (max(v4, v1[v7] - a1[(a1 + v7) % len(a1)]), max(v5, v1[v7] + a1[(a1 + v7) % len(a1)]))
                    v6[v7 + 1] = max(v6[v7], v4 + a1[(a1 + v7) % len(a1)], v5 - a1[(a1 + v7) % len(a1)])
                v1 = v6
                v2 = max(v2, v1[-1])
            return v2
        v1 = min(range(len(a1)), key=lambda x: a1[x])
        return max(best_time_to_buy_and_sell_stock_v(v1), best_time_to_buy_and_sell_stock_v(v1 + 1))
