a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0 (float)
print(a // b)  # 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the reminder after integer division

print()

print(a + b / 3 - 4 * 12)           # - 35.0 due to operator precedence
print(a+(b/3)-(4*12))               # - 35.0
print((((a + b) / 3) - 4) * 12)     # 12.0

c = a + b
d = c / 3
e = d - 4
print(e * 12)

