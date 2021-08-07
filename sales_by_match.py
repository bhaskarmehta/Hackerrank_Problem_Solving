def sockMerchant(n, ar):
    # Write your code here
    l = []
    pair = 0
    count = 0
    for i in range(1, 101):
        count = 0
        for j in range(0, n):
            if i == ar[j]:
                count += 1
        l.append(count)

    for k in range(0, 100):
        pair += l[k] // 2
    return pair
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9,ar))
