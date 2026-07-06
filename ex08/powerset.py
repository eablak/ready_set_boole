def powerset(s):

    x = len(s)
    b = []

    for i in range(1 << x):
        b.append(set(([s[j] for j in range(x) if (i & (1 << j))])))

    return b


if __name__ == "__main__":

    a = {1, 43, 6, 8, 1}
    print(powerset(list(a)))
