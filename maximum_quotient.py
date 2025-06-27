class MaximumQuotient:
    def __init__(self, num_arr):
        self.num_arr = num_arr
        self.n = len(num_arr)
        self.min_memo = [[-1 for i in range(self.n)] for j in range(self.n)]
        self.max_memo = [[-1 for i in range(self.n)] for j in range(self.n)]
        self.print_max_memo = [["m" for i in range(self.n)] for j in range(self.n)]
        self.print_min_memo = [["m" for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            self.min_memo[i][i] = self.max_memo[i][i] = self.num_arr[i]  # base cases, i = j
            self.print_max_memo[i][i] = self.print_min_memo[i][i] = str(self.num_arr[i])
        self.max_value = self.max_segment(0, self.n - 1)
        self.min_value = self.min_segment(0, self.n - 1)
        self.max_string = self.print_max_memo[0][self.n - 1]
        self.min_string = self.print_min_memo[0][self.n - 1]

    def max_segment(self, i, j) -> float:
        if self.max_memo[i][j] == -1:  # not computed
            temp_max = float('-inf')
            temp_pos = i
            for k in range(i, j):  # splits can only go from i to j - 1
                curr = self.max_segment(i, k) / self.min_segment(k + 1, j)
                if curr > temp_max:
                    temp_max = curr
                    temp_pos = k

            self.max_memo[i][j] = temp_max

            if j == i + 1:
                self.print_max_memo[i][j] = (self.print_max_memo[i][temp_pos] +
                                             " / " + self.print_min_memo[temp_pos + 1][j])
            elif temp_pos == i:
                self.print_max_memo[i][j] = (self.print_max_memo[i][temp_pos] +
                                             " / (" + self.print_min_memo[temp_pos + 1][
                    j] + ")")
            elif j == temp_pos + 1:
                self.print_max_memo[i][j] = ("(" + self.print_max_memo[i][temp_pos] +
                                             ") / " + self.print_min_memo[temp_pos + 1][j])
            else:
                self.print_max_memo[i][j] = ("(" + self.print_max_memo[i][temp_pos] +
                                             ") / (" + self.print_min_memo[temp_pos + 1][j] + ")")

        return self.max_memo[i][j]

    def min_segment(self, i, j) -> float:
        if self.min_memo[i][j] == -1:  # not computed
            temp_min = float('inf')
            temp_pos = i
            for k in range(i, j):
                curr = self.min_segment(i, k) / self.max_segment(k + 1, j)
                if curr < temp_min:
                    temp_min = curr
                    temp_pos = k

            self.min_memo[i][j] = temp_min

            if j == i + 1:
                self.print_min_memo[i][j] = (self.print_min_memo[i][temp_pos] + " / " +
                                             self.print_max_memo[temp_pos + 1][j])
            elif temp_pos == i:
                self.print_min_memo[i][j] = (self.print_min_memo[i][temp_pos] +
                                             " / (" + self.print_max_memo[temp_pos + 1][j] + ")")
            elif j == temp_pos + 1:
                self.print_min_memo[i][j] = ("(" + self.print_min_memo[i][temp_pos] +
                                             ") / " + self.print_max_memo[temp_pos + 1][j])
            else:
                self.print_min_memo[i][j] = ("(" + self.print_min_memo[i][temp_pos] +
                                             ") / (" + self.print_max_memo[temp_pos + 1][j] + ")")

        return self.min_memo[i][j]


def maximum_quotient(a):
    temp = MaximumQuotient(a)
    return temp.max_string


def minimum_quotient(a):
    temp = MaximumQuotient(a)
    return temp.min_string
