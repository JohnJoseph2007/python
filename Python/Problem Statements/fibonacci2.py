def fibonacci(n):
    f = [0, 1]
    for i in range(2, n):
        q = f[i-1]+f[i-2]
        f.append(q)
    print(f)

fibonacci(10)