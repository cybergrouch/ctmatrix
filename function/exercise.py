import math

def quadratic(a, b, c):
  discriminant = math.sqrt(b*b - 4*a*c)
  return ((-b + discriminant) / (2*a), (-b - discriminant) / (2*a))

def print_greater_quadratic(L):
  for a, b, c in L:
    plus, minus = quadratic(a, b, c)
    if plus > minus:
      print(plus)
    else:
      print(minus)
