def int_or_dec(x, y):
    if x % y == 0:
        return "integer"
    return "decimal"


a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
result = int_or_dec(a, b)
print(f"The result of {a} / {b} is a {result}")
