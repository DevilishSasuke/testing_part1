import pytest
from roots import calc_roots

def test_two_roots_success():
  assert calc_roots(1, -3, 2) == (2, 1)
  assert calc_roots(1, 5, 6) == (-2, -3)

def test_one_root_success():
  res = calc_roots(1, -2, 1)
  assert res[0] == res[1] == 1

def test_zero_roots_success():
  assert calc_roots(1, 1, 1) is None

def test_zero_division_exc():
  with pytest.raises(ValueError, match="a cannot be 0, will invoke zero division"):
    calc_roots(0, 2, 3)

def test_wrong_type_exc():
  with pytest.raises(TypeError, match="args must be numeric values"):
    calc_roots("a", "b", "c")