def two_sum_sorted(lst, target):
    left = 0
    right = len(lst) - 1

    while left < right:
        current_sum = lst[left] + lst[right]

        if current_sum == target:
            return left, right

        elif current_sum < target:
            left += 1

        else:
            right -= 1

    return None

def remove_duplicates(lst):
    write = 0

    for read in range(1, len(lst)):

        if lst[write] != lst[read]:
            write += 1
            lst[write] = lst[read]

    return write + 1

def sorted_squares(lst):
    left = 0
    right = len(lst) - 1
    write = len(lst) - 1

    result = [0] * len(lst)

    while left <= right:
        if abs(lst[left]) > abs(lst[right]):
            result[write] = lst[left] ** 2
            left += 1
        else:
            result[write] = lst[right] ** 2
            right -= 1

        write -= 1

    return result