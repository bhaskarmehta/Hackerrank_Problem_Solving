def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    count = 1
    l = []
    pair = 0

    for i in range(0, n - 1):
        temp = ar[i]

        if temp == ar[i + 1]:
            count += 1
            if i==n-2:
                l.append(count)
        else:
            l.append(count)
            count = 1

    for j in range(0, len(l)):
        pair += l[j] // 2
    print(pair)
    print(l)

ar=[10, 20, 20, 10, 10, 50, 50, 10, 20]
print(sockMerchant(9,ar))
