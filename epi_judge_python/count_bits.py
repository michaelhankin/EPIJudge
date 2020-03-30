from test_framework import generic_test


# Returns the number of set bits in a non-negative integer
def count_bits(x: int) -> int:
    set = 0
    while x > 0:
        set += (x & 1)
        x >>= 1

    return set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
