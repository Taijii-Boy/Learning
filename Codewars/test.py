
def solve(arr):
    result_lists = []
    for i, first in enumerate(arr, 1):
        for second in arr[i:]:
            third = 2 * second - first
            if third in arr:
                result_lists.append([first, second, third])
    return len(result_lists)


print(solve([0, 1, 4, 5, 7, 9, 10, 13, 15, 16, 18, 19]))
