def pythagoreanTriplets(n):
  for b in range(n):
    for a in range(1, b):
        c = math.sqrt(a * a + b * b)
        if c % 1 == 0:
            print(a, b, int(c))
def pythagoreanTripletsCheck(a, b, c):
    return True if a * a + b * b == c * c else False
    
