"""

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-02-28 22:15:00

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-02-28 22:15:00

@Title : Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

"""


def setzeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row_set = set()
    col_set = set()
    m = len(matrix)
    n = len(matrix[0])
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                row_set.add(row)
                col_set.add(col)

    for row in range(m):
        for col in range(n):
            if row in row_set or col in col_set:
                matrix[row][col] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setzeroes(matrix)
    print(matrix)
