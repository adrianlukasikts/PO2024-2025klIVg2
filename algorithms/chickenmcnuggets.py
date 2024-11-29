import sys


def num_boxes(order: int):
    dp = [sys.maxsize for _ in range(21)]
    dp[6] = 1
    dp[9] = 1
    dp[12] = 2
    dp[15] = 2
    dp[18] = 2
    dp[20] = 1

    for i in range(21, order + 1):
        minimum: int = sys.maxsize
        if minimum > dp[i - 6]:
            minimum = dp[i - 6]
        if minimum > dp[i - 9]:
            minimum = dp[i - 9]
        if minimum > dp[i - 20]:
            minimum = dp[i - 20]
        if minimum == sys.maxsize:
            dp.append(minimum)
        else:
            dp.append(minimum + 1)
    return dp[order]

print(num_boxes(43))