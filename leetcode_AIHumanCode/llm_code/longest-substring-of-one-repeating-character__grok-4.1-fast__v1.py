class SegmentTree:
    def __init__(self, text):
        self.length = len(text)
        self.data = [None] * (4 * self.length)
        self._build(1, 0, self.length - 1, text)

    def _build(self, node_id, left_bound, right_bound, text):
        if left_bound == right_bound:
            ch = text[left_bound]
            self.data[node_id] = [ch, ch, 1, 1, 1, 1]
            return
        mid_point = (left_bound + right_bound) // 2
        self._build(2 * node_id, left_bound, mid_point, text)
        self._build(2 * node_id + 1, mid_point + 1, right_bound, text)
        self.data[node_id] = self._merge(self.data[2 * node_id], self.data[2 * node_id + 1])

    def _merge(self, left_node, right_node):
        l_start_char, l_end_char, l_prefix_run, l_suffix_run, l_segment_size, l_max_run = left_node
        r_start_char, r_end_char, r_prefix_run, r_suffix_run, r_segment_size, r_max_run = right_node
        merged_start_char = l_start_char
        merged_end_char = r_end_char
        merged_prefix_run = l_prefix_run + r_prefix_run if l_prefix_run == l_segment_size and l_end_char == r_start_char else l_prefix_run
        merged_suffix_run = r_suffix_run + l_suffix_run if r_suffix_run == r_segment_size and r_start_char == l_end_char else r_suffix_run
        merged_segment_size = l_segment_size + r_segment_size
        merged_max_run = max(l_max_run, r_max_run, l_suffix_run + r_prefix_run if l_end_char == r_start_char else 0)
        return [merged_start_char, merged_end_char, merged_prefix_run, merged_suffix_run, merged_segment_size, merged_max_run]

    def change(self, index, new_ch):
        self._change(1, 0, self.length - 1, index, new_ch)

    def _change(self, node_id, left_bound, right_bound, index, new_ch):
        if left_bound == right_bound:
            self.data[node_id] = [new_ch, new_ch, 1, 1, 1, 1]
            return
        mid_point = (left_bound + right_bound) // 2
        if index <= mid_point:
            self._change(2 * node_id, left_bound, mid_point, index, new_ch)
        else:
            self._change(2 * node_id + 1, mid_point + 1, right_bound, index, new_ch)
        self.data[node_id] = self._merge(self.data[2 * node_id], self.data[2 * node_id + 1])

    def current_max(self):
        return self.data[1][5]


class Solution:
    def longestRepeating(self, initial_string, update_chars, update_positions):
        seg_tree = SegmentTree(initial_string)
        answers = []
        for updated_char, pos in zip(update_chars, update_positions):
            seg_tree.change(pos, updated_char)
            answers.append(seg_tree.current_max())
        return answers
