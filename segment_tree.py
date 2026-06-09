class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        q1 = self.query(2 * node + 1, start, mid, left, right)
        q2 = self.query(2 * node + 2, mid + 1, end, left, right)
        return q1 + q2

    def update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2

            if index <= mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)

            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


arr = [1, 3, 5, 7, 9, 11]

st = SegmentTree(arr)

print(st.query(0, 0, st.n - 1, 1, 3))  # sum from index 1 to 3 = 15

st.update(0, 0, st.n - 1, 1, 10)

print(st.query(0, 0, st.n - 1, 1, 3))  # now 10 + 5 + 7 = 22
