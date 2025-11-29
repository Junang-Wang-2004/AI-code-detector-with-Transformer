class Solution:
    def topStudents(self, positive_feedback, negative_feedback, reports, student_ids, k):
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)
        scored = []
        for idx, text in zip(student_ids, reports):
            parts = text.split()
            pts = 0
            for term in parts:
                if term in pos_set:
                    pts += 3
                elif term in neg_set:
                    pts -= 1
            scored.append((pts, idx))
        scored.sort(key=lambda pair: (-pair[0], pair[1]))
        return [idx for _, idx in scored[:k]]
