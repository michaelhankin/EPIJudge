import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            equal, smaller = equal + 1, smaller + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


def variant1(A: List[int]) -> None:
    curr_i = 0
    curr = A[curr_i]
    for i in range(len(A)):
        if A[i] == curr:
            A[i], A[curr_i] = A[curr_i], A[i]
            curr_i += 1
    curr = A[curr_i]
    for i in range(curr_i, len(A)):
        if A[i] == curr:
            A[i], A[curr_i] = A[curr_i], A[i]
            curr_i += 1


def variant2(A: List[int]) -> None:
    curr_i = 0
    curr = A[curr_i]
    for i in range(len(A)):
        if A[i] == curr:
            A[i], A[curr_i] = A[curr_i], A[i]
            curr_i += 1
    curr = A[curr_i]
    for i in range(curr_i, len(A)):
        if A[i] == curr:
            A[i], A[curr_i] = A[curr_i], A[i]
            curr_i += 1
    curr = A[curr_i]
    for i in range(curr_i, len(A)):
        if A[i] == curr:
            A[i], A[curr_i] = A[curr_i], A[i]
            curr_i += 1


def variant3(A: List[bool]) -> None:
    start = 0
    for i in range(len(A)):
        if not A[i]:
            A[start], A[i] = A[i], A[start]
            start += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
