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
            if current_len < min_len:
                min_len = current_len

            window_sum -= lst[start]
            start += 1

    if min_len == inf:
        return 0

    return min_len
