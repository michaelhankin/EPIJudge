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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
