from math import inf

#To find the length of the smallest contiguous subarray whose sum is greater than or equal to S
def smallest_subarray(lst, s):
    start = 0
    min_len = inf
    window_sum = 0

    for end in range(len(lst)):
        window_sum += lst[end]

        while window_sum >= s:
            current_len = (end - start + 1)
            min_len = min(min_len, current_len)

            window_sum -= lst[start]
            start += 1

    if min_len == inf:
        return 0

    return min_len

# To find the length of the longest substring with no repeated characters.
def longest_unique_substring(string):
    start = 0
    window = {}
    max_len = 0

    for end in range(len(string)):
        char = string[end]

        if char in window and window[char] >= start:
            start = window[char] + 1

        window[char] = end

        current_len = end - start + 1
        max_len = max(max_len, current_len)

    return max_len