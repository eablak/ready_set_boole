def multiplier(a: int, b: int) -> int:

    result = 0

    while (b > 0):
        if b & 1:
            result += a

        a = a << 1
        b = b >> 1

    return result


if __name__ == "__main__":
    a = 132
    b = 501

    if a > 0 and b > 0:
        print(multiplier(a, b))