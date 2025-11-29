class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        priority = ["electronics", "grocery", "pharmacy", "restaurant"]
        candidates = []
        length = len(code)
        for idx in range(length):
            coupon = code[idx]
            biz_type = businessLine[idx]
            status = isActive[idx]
            if (status and
                coupon and
                biz_type in priority and
                all(char.isalnum() or char == '_' for char in coupon)):
                prio_rank = priority.index(biz_type)
                candidates.append((prio_rank, coupon))
        candidates.sort()
        return [item[1] for item in candidates]
