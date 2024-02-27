"""

@Author: Kolapati Mani Deepak Chandu

@Date: 2024-02-27 21:47:00

@Last Modified by: Kolapati Mani Deepak Chandu

@Last Modified time: 2024-02-27 21:47:00

@Title : Find Longest Substring Without Repeating Characters

"""


def lengthOfLongestSubstring(s: str) -> tuple[str, int]:
    """
    Find Longest Substring Without Repeating Characters

    Parameters:
    -

    Returns:
    -
    """
    longest_length = 0
    longest_substring = ""
    for i in range(len(s)):
        substring = s[i]
        length = 1
        if (len(s) - i) <= longest_length:
            break
        for j in range(i + 1, len(s)):
            if s[j] not in substring:
                substring += s[j]
                length += 1
            else:
                break
        if length > longest_length:
            longest_substring = substring
            longest_length = length
    return longest_substring, longest_length


if __name__ == "__main__":
    s = "abcabcbb"
    substring, substring_length = lengthOfLongestSubstring(s)
    print(substring, substring_length)
