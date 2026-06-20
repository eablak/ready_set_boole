def gray_code(n: int)-> int:
    return n ^ (n >> 1)


if __name__ == "__main__":
    n = 5

    if n > 0:
        print(gray_code(n))