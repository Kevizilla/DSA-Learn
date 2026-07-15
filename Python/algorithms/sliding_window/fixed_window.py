def max_sum_subarray(lst, k):
    if not lst:
        return "Enter valid list"

    if k <= 0:
        return "k has to be greater than 0"

    if k > len(lst):
        return "k cannot be greater than len(lst)"

    # Compute the first window's sum
    current_sum = sum(lst[:k])
    max_sum = current_sum
    # Slide the window one step at a time
    for i in range(0, len(lst)-k):
        current_sum = current_sum - lst[i] + lst[i+k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum