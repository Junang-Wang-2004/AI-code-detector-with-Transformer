class Solution:
    def displayTable(self, order_list):
        table_set = set()
        dish_set = set()
        for cust, tbl, dish in order_list:
            table_set.add(int(tbl))
            dish_set.add(dish)
        sorted_tables = sorted(table_set)
        sorted_dishes = sorted(dish_set)
        counts = {t: {d: 0 for d in sorted_dishes} for t in sorted_tables}
        for cust, tbl, dish in order_list:
            t = int(tbl)
            counts[t][dish] += 1
        res = [["Table"] + sorted_dishes]
        for t in sorted_tables:
            row = [str(t)]
            for d in sorted_dishes:
                row.append(str(counts[t][d]))
            res.append(row)
        return res
