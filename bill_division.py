def bonAppetit(bill, k, b):
    # Write your code here
    total_bill = 0
    for i in range(0, len(bill)):
        total_bill += bill[i]
    if b == (total_bill - bill[k]) / 2:
        print("Bon Appetit")

    else:
        print(b - ((total_bill - bill[k]) // 2))
bill=[3 ,10 ,2 ,9]
bonAppetit(bill, 1, 12)
