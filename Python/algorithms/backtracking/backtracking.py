def generate_subsets(lst):
    result = []
    current = []

    def backtrack(index):

        # Base case
        if index == len(lst):
            result.append(current.copy())
            return

        # Choice 1: Take the current element
        current.append(lst[index])
        backtrack(index + 1)
        current.pop()

        # Choice 2: Skip the current element
        backtrack(index + 1)


    backtrack(0)
    return result