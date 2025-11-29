class Solution:
    def getNumberOfBacklogOrders(self, orders):
        MOD = 10**9 + 7
        bids = []
        asks = []
        for price, amount, typ in orders:
            if typ == 0:
                bids.append([price, amount])
            else:
                asks.append([price, amount])
        bids.sort(key=lambda x: x[0], reverse=True)
        asks.sort(key=lambda x: x[0])
        ptr_b = 0
        ptr_a = 0
        while ptr_b < len(bids) and ptr_a < len(asks):
            if bids[ptr_b][0] >= asks[ptr_a][0]:
                transact = min(bids[ptr_b][1], asks[ptr_a][1])
                bids[ptr_b][1] -= transact
                asks[ptr_a][1] -= transact
                if bids[ptr_b][1] == 0:
                    ptr_b += 1
                if asks[ptr_a][1] == 0:
                    ptr_a += 1
            else:
                break
        result = 0
        for entry in bids + asks:
            result = (result + entry[1]) % MOD
        return result
