"""

@Author: Kolapati Mani Deepak Chandu

@Title : In Pascal's triangle, each number is the sum of the two numbers directly above it

"""
import sys
sys.setrecursionlimit(10000)


def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    arr = [1 for i in range(numRows)]
    pascal_array = generate(numRows - 1)
    prev_arr = pascal_array[-1]
    for i in range(1, len(arr) - 1):
        arr[i] = prev_arr[i - 1] + prev_arr[i]
    pascal_array.append(arr)
    return pascal_array


def print_pascals(numRows):
    for row in range(1, numRows):
        print(generate(row))


if __name__ == "__main__":
    rows = int(input("Enter the no of rows : "))
    print_pascals(rows)


"""
Output
Enter the no of rows : 10
[[1]]
[[1], [1, 1]]
[[1], [1, 1], [1, 2, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]

Process finished with exit code 0 """

