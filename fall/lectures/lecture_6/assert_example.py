def division(a, b):
    assert b != 0, "Division by zero is not supported"
    print("Below assertion")
    return a / b

print(division(1, 0))

