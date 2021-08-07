def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26" + "." + "09" + "." + str(year)

    lpYR = 0
    if year % 4 == 0:
        lpyr = 1
        if (year >= 1919):
            if (year % 100 == 0 and year % 400 != 0):
                lpyr = 0;

    else:
        lpyr = 0;

    if (lpyr == 0):
        return "13" + "." + "09" + "." + str(year)
    else:
        return "12" + "." + "09" + "." + str(year)
print(dayOfProgrammer(2016))