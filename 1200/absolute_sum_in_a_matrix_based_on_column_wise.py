for _ in range(int(input())):
    n, m = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(n)]
    s = list(zip(*s))
    ans = 0
    for i in s:
        for j, v in enumerate(sorted(i)):
            ans += (n - 1 - j - j) * v
    print(-ans)