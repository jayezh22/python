a = 100  # Assigning initial value to variable 'a'

# Compound assignment operators
a += 10  # Equivalent to: a = a + 10
print(a)  # Output: 110

a -= 10  # Equivalent to: a = a - 10
print(a)  # Output: 100

a *= 10  # Equivalent to: a = a * 10
print(a)  # Output: 1000

a /= 10  # Equivalent to: a = a / 10
print(a)  # Output: 100.0

a %= 10  # Equivalent to: a = a % 10
print(a)  # Output: 0.0

a //= 10  # Equivalent to: a = a // 10
print(a)  # Output: 0.0

a **= 10  # Equivalent to: a = a ** 10
print(a)  # Output: 0.0

# Bitwise assignment operators (commented out for syntax error demonstration)
"""
a &= 10   # Equivalent to: a = a & 10
a |= 10   # Equivalent to: a = a | 10
a ^= 10   # Equivalent to: a = a ^ 10
a >>= 10  # Equivalent to: a = a >> 10
a <<= 10  # Equivalent to: a = a << 10
"""

# Assignment expression (Python 3.8+ feature)
print(a := 5)  # Output: 5

print(a)  # Output: 5
