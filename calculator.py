hexa_1 = input("enter a  number ")
hexa_2 = input("enter a number")
a = int(hexa_1,16)
b = int(hexa_2,16)
print("\nArithmetic Operations")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Exponent:", a **b)
print("Floor Division:", a //b)
print("\nAssignment Operations")
a += b
print("After a += b :", a)
a -= b
print("After a -= b :", a)
a *= b
print("After a *= b :", a)
a /= b
print("After a /= b :", a)
a%= b
print("After a %= b :", a)
a **= b
print("After a **= b :", a)
a //= b
print("After a //= b :", a)
