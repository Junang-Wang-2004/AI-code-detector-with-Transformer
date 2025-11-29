from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions):
        MAX_AMOUNT = 1000
        TIME_LIMIT = 60
        name_to_txs = defaultdict(list)
        for trans_str in transactions:
            name, time_str, amt_str, city = trans_str.split(',')
            time = int(time_str)
            amt = int(amt_str)
            name_to_txs[name].append((time, amt, city))
        result = []
        for name, txs in name_to_txs.items():
            txs.sort(key=lambda x: x[0])
            m = len(txs)
            left = 0
            right = 0
            for i in range(m):
                t_time, t_amt, t_city = txs[i]
                if t_amt > MAX_AMOUNT:
                    result.append(f"{name},{t_time},{t_amt},{t_city}")
                    continue
                while left < m and txs[left][0] < t_time - TIME_LIMIT:
                    left += 1
                while right < m and txs[right][0] <= t_time + TIME_LIMIT:
                    right += 1
                has_diff_city = any(txs[j][2] != t_city for j in range(left, right))
                if has_diff_city:
                    result.append(f"{name},{t_time},{t_amt},{t_city}")
        return result
