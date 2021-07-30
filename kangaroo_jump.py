def kangaroo(x1, v1, x2, v2):
    # Write your code here
    print("Hello")

    if v2 >= v1:
        return "NO"
    else:

            while x1!=x2 and x1<=x2:
                x1 = x1 + v1

                x2 = x2 + v2
            if x1==x2:
                return "Yes"

            else:
                return "NO"



print(kangaroo(0 ,3, 4, 2))