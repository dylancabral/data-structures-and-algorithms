import pytest
from data_structures.sorting import insertion_sort, merge, merge_sort

def test_exists():
    assert insertion_sort

def test_insertion_one():
  assert insertion_sort([-5, 0, 12, 6, -3]) == [-5, -3, 0, 6, 12]

def test_insertion_sort_2():
  assert insertion_sort([8, 4, 23, 42, 16, 15]) == [4, 8, 15, 16, 23, 42]

def test_insertion_sort_3():
  assert insertion_sort([1,2,3,4,5]) == [1,2,3,4,5]

def test_insertion_sort_4():
  assert insertion_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_insertion_sort_5():
  assert insertion_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_insertion_sort_6():
  assert insertion_sort([100]) == [100]

def test_insertion_sort_7():
  assert insertion_sort([]) == []


def test_merge_sort():
  assert merge_sort([1,2,3,4,5]) == [1,2,3,4,5]

def test_merge_sort_1():
  assert merge_sort([5,4,3,2,1]) == [1,2,3,4,5]

def test_merge_sort_2():
  assert merge_sort([1,9,7,6,8]) == [1,6,7,8,9]

def test_merge_sort_3():
  assert merge_sort([100]) == [100]

def test_merge_sort4():
  assert merge_sort([]) == []
