def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d
    return current_gcd

def gcd(a, b):
    if min(a, b) == 0:
        return max(a, b)
    else:
        return gcd(min(a, b),  max(a, b) % min(a, b))
