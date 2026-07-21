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

    def combination_sum(lst,  target):
        result = []
        current = []
        index = 0
        remaining = target

        def backtrack(index, remaining):
            if ...:
                ...

            # Take current number
            ...

            backtrack(_____, _____)

            ...

            # Skip current number
            backtrack(_____, _____)
