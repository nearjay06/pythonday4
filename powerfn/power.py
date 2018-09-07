def multiply_items(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    else:
        return a*multiply_items(a, b-1)


print(multiply_items(3, 4))
print(multiply_items(2, 3))
