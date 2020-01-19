def lcm(a, b):
    constant = a
    print(f'const = {constant}')
    while a % b != 0:
        a = a + constant
        print(f'a = {a}')
    return a

