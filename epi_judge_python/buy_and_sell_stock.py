from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    curr_min = prices[0]
    max_profit = 0.0
    for price in prices[1:]:
        curr_profit = price - curr_min
        max_profit = max(max_profit, curr_profit)
        curr_min = min(curr_min, price)
    return max_profit


def variant1(nums: List[int]) -> int:
    if not nums:
        return 0
    max_length, curr_length, prev_num = 0, 0, None
    for num in nums:
        if num == prev_num:
            curr_length += 1
        else:
            max_length = max(max_length, curr_length + 1)
            curr_length = 0
            prev_num = num
    return max(max_length, curr_length + 1)


print('Variant 1 tests')
print('[3, 7, 2, 2, 0, 4, 4, 4] ->',
      variant1([3, 7, 2, 2, 0, 4, 4, 4]))
print('[3, 3, 7, 2, 2, 0, 0, 4, 4] ->',
      variant1([3, 3, 7, 2, 2, 0, 0, 4, 4]))
print('[] ->', variant1([]))
print('[2, 2, 2, 1, 5, 7] ->', variant1([2, 2, 2, 1, 5, 7]))
print()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
