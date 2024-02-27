"""

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-02-27 20:47:00

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-02-27 21:13:00

@Title : Removes duplicates from a given list of integers and updates the list in-place.

"""


def remove_duplicates(nums: list[int]) -> int:
    """Removes duplicates from a given list of integers and updates the list in-place.

    Parameters:
    - nums (list[int]): The input list containing integers.

    Returns:
    - int: The length of the modified list with unique elements. """
    length = len(nums)
    if length <= 1:
        return length
    unique_nums = [nums[0]]
    unique_nums.extend([nums[i] for i in range(1, length) if nums[i] != nums[i-1]])
    nums[:] = unique_nums
    return len(nums)


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 4, 4, 4, 4, 5, 5, 5, 8, 8, 8, 10]
    remove_duplicates(nums)
    print(nums)

