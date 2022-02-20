def knapsack(idx, cap_left):
    ret1, ret2 = 0, 0
    if idx >= n:
        return 0

    if weight[idx] <= cap_left:
        ret1 = price[idx] + knapsack(idx+1, cap_left-weight[idx])

  
    ret2 = knapsack(idx+1, cap_left)

    return max(ret1, ret2)


n = int(input("Enter the number of items: "))
price = []
weight = []
for i in range(n):
    p, w = input().split(' ')  # price wight
    price.append(int(p))
    weight.append(int(w))

cap = int(input("Enter the capacity of knapsack: "))

ans = knapsack(0, cap)   #(index, capacity left)
print("Maximum price you can get", ans)