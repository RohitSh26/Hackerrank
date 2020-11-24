"""
problem statement - given score sheet, find runner-up score.

Input:
n scores, store scores in the list

output:
returns the second highest score
"""


def get_second_highest_score(n, arr):
    if 2 <= n <= 10:
        if -100 <= arr[0] <= 100:
            if -100 <= arr[1] <= 100:
                max_val = max(arr[0], arr[1])
                second_max_val = min(arr[0], arr[1])

                for i in range(2, len(arr)):
                    if -100 <= arr[i] <= 100:
                        # check if value at index is greater than max
                        # second_max will become max
                        if arr[i] > max_val:
                            second_max_val = max_val
                            max_val = arr[i]
                        # check value at index is greater than second max and not already a max value
                        elif (arr[i] > second_max_val) and (arr[i] != max_val):
                            second_max_val = arr[i]

    return second_max_val


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(get_second_highest_score(n, list(arr)))
