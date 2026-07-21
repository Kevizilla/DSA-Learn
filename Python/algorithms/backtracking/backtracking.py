from pip._internal.models import index


def generate_subsets(lst):
    result = []
    current = []

    def _backtrack(index):

        # Base case
        if index == len(lst):
            result.append(current.copy())
            return

        # Choice 1: Take the current element
        current.append(lst[index])
        _backtrack(index + 1)
        current.pop()

        # Choice 2: Skip the current element
        _backtrack(index + 1)


    _backtrack(0)
    return result

def generate_permutations(lst):
    result = []
    current = []
    used = set()

    def backtrack():
        if len(lst) == len(current):
            result.append(current.copy())
            return

        for num in lst:
            if num in used:
                continue
            current.append(num)
            used.add(num)
            backtrack()
            used.remove(current.pop())

def combination_sum(nums, target):
    result = []
    current = []

    def backtrack(index, remaining):
        # Base cases
        if remaining == 0:
            result.append(current.copy())
            return

        if remaining < 0 or index == len(nums):
            return

        num = nums[index]
        current.append(num)
        backtrack(index, remaining - num)

        current.pop()
        backtrack(index + 1, remaining)

    backtrack(0, target)
    return result

def is_safe(board, row, col):
    current_row = row -1
    current_col = col
    while current_row >= 0:
        if board[current_row][col] == "Q":
            return False
        current_row -= 1

    current_col = col - 1
    current_row = row - 1

    while current_row >= 0 and current_col >= 0:
        if board[current_row][current_col] == "Q":
            return False
        current_row -= 1
        current_col -= 1

    current_col = col + 1
    current_row = row - 1
    while current_row >= 0 and current_col < len(board[0]):
        if board[current_row][current_col] == "Q":
            return False
        current_row -= 1
        current_col += 1

    return True
