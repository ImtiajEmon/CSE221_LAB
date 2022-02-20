def dp(m):
    if m == 0:
        return 0

    if memo[m] != -1:
        return memo[m]

    ans = 100000000  # we need min so we take max val
    for c in coin:
        if c > m:    # coin value can be grater than remain amount
            continue
        ans = min(ans, 1 + dp(m-c))
        
    memo[m] = ans
    return ans

n = int(input("Enter the number of coin: "))
coin = []
for i in range(n):
    coin.append(int(input()))

m = int(input("Enter the amount you want to make: "))

memo = [-1] * (m+10)
ans = dp(m)
if(ans > m):
    print("Change can't possible.")
else:
    print("The minimum nuber of coin is", ans)