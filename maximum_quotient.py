class MaximumQuotient:
    def __init__(self, num_arr):
        self.num_arr = num_arr
        self.n = len(num_arr)
        self.min_memo = [[None] * self.n for i in range(self.n)]
        self.max_memo = [[None] * self.n for i in range(self.n)]
        for i in range(self.n):
            self.min_memo[i][i] = self.max_memo[i][i] = self.num_arr[i]  # base cases, i = j
        self.max_value = self.max_segment(0, self.n - 1)
        self.min_value = self.min_segment(0, self.n - 1)

    def max_segment(self, i, j):
        if self.max_memo[i][j] is None:  # not computed
            res = float('-inf')
            for k in range(i, j):  # splits can only go from i to j - 1
                curr = self.max_segment(i, k) / self.min_segment(k + 1, j)
                res = max(res, curr)

            self.max_memo[i][j] = res

        return self.max_memo[i][j]

    def min_segment(self, i, j):
        if self.min_memo[i][j] is None:  # not computed
            res = float('inf')
            for k in range(i, j):
                curr = self.min_segment(i, k) / self.max_segment(k + 1, j)
                res = min(res, curr)

            self.min_memo[i][j] = res

        return self.min_memo[i][j]
