def adder(a: int, b: int) -> int:
    
    mask = 0xffffffff

    while (b & mask) != 0:
        
        carry = (a & b)
        sum = (a ^ b)

        a = sum
        b = carry << 1

    return a


if __name__ == "__main__":
    
    a = 132
    b = 501

    if a > 0 and b > 0:
        print(adder(a, b))