
def first_non_zero_element(row):
    for element in row:
        if element != 0:
            return element
    return 0


def first_non_zero_index(row):
    for index in range(len(row)):
        if row[index] != 0:
            return index
    return -1


def order_zeros(matrix):
    for index1 in range(matrix.row_count):
        non_zero_index_r1 = first_non_zero_index(matrix.data[index1])
        for index2 in range(index1 + 1, matrix.row_count):
            non_zero_index_r2 = first_non_zero_index(matrix.data[index2])
            if non_zero_index_r2 != -1 and (non_zero_index_r1 > non_zero_index_r2 or non_zero_index_r1 == -1):
                matrix.swap_rows(index1, index2)


def make_pivot(matrix, row, col):
    element = matrix.data[row][col]
    if element != 0:
        matrix.mul_row(row, 1 / element)
        for row2 in range(matrix.row_count):
            if row2 != row:
                element2 = matrix.data[row2][col]
                matrix.add_row(row2, row, -element2)
        return True
    return False


def reduced_echelon(matrix):
    reduced_matrix = Matrix(matrix.data)
    order_zeros(reduced_matrix)
    col = 0
    for row in range(0, reduced_matrix.row_count):
        while col < reduced_matrix.col_count and not make_pivot(reduced_matrix, row, col):
            col = col + 1
        col = col + 1
        order_zeros(reduced_matrix)
    return reduced_matrix


class Matrix:
    def __init__(self, data):
        self.row_count = len(data)
        self.col_count = len(data[0])
        self.data = []
        for index in range(self.row_count):
            self.data.append(data[index].copy())

    def mul_row(self, r, scalar):
        for i in range(self.col_count):
            self.data[r][i] = scalar * self.data[r][i]

    def add_row(self, r1, r2, scalar):
        for i in range(self.col_count):
            self.data[r1][i] = self.data[r1][i] + scalar * self.data[r2][i]

    def swap_rows(self, r1, r2):
        self.data[r1], self.data[r2] = self.data[r2], self.data[r1]

    def print(self):
        for row in self.data:
            for element in row:
                print(element, end="  ")
            print()

