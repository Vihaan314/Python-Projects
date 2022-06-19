def HCF(a, b):
    a, b = max(a, b), min(a, b)
    while b!=0:
        a, b = b, a % b
    return a
def LCM(a, b):
    return (a*b)/HCF(a, b)

print(HCF(18, 27))
print(LCM(2, 3))
