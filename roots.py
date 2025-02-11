import math
import sys
from typing import Tuple

permitted_types = [type(int), type(float)]
def calc_roots(a: float, b: float, c: float) -> Tuple[float, float] | None:
  """
    solve the quadratic equations
    returns 2 roots (can be equal => have only 1 root), or none
  """
  if (type(a) not in permitted_types or
      type(b) not in permitted_types or
      type(c) not in permitted_types):
      raise TypeError("args must be numeric values")
  
  if abs(a) < sys.float_info.epsilon:
     raise ValueError("a cannot be 0, will invoke zero division")
  
  D = b ** 2 - 4 * a * c

  if D < 0:
     return None
  elif D < sys.float_info.epsilon:
     x = -b / (2 * a)
     return (x, x)
  else:
     x1 = (-b + math.sqrt(D)) / (2 * a)
     x2 = (-b - math.sqrt(D)) / (2 * a)
     return (x1, x2)
  
