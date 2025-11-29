class Solution:
    def shoppingOffers(self, price, special, needs):
        from functools import lru_cache
        items = len(price)
        @lru_cache(None)
        def best_cost(req):
            if all(q == 0 for q in req):
                return 0
            total = sum(price[k] * req[k] for k in range(items))
            for deal in special:
                if all(req[k] >= deal[k] for k in range(items)):
                    nxt_req = tuple(req[k] - deal[k] for k in range(items))
                    total = min(total, deal[-1] + best_cost(nxt_req))
            return total
        return best_cost(tuple(needs))
