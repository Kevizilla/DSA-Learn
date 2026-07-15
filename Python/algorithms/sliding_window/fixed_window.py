def max_sum_subarray(lst, k):
    if not lst:
        return "Enter valid list"

    if k <= 0:
        return "k has to be greater than 0"

    if k > len(lst):
        return "k cannot be greater than len(lst)"

    current_sum = sum(lst[:k])
    max_sum = current_sum
    for i in range(k, len(lst)):
        current_sum = current_sum + lst[i] - lst[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

def average_of_subarray(lst, k):
    if not lst:
        return "Enter valid list"

    if k <= 0:
        return "k has to be greater than 0"

    if k > len(lst):
        return "k cannot be greater than len(lst)"

    current_sum = sum(lst[:k])
    result = [current_sum/k]

    for i in range(k, len(lst)):
        current_sum = current_sum + lst[i] - lst[i - k]
        result.append(current_sum/k)

    return result
