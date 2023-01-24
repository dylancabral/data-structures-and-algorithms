import pytest
from data_structures.insertion_sort import insertion_sort

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
