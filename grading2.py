def gradingStudents(grades):
    # Write your code here
    for i in range(0,len(grades)):
        if(grades[i]>=38):
                diff=5-(grades[i]%5)
                if diff<3:
                    grades[i]=grades[i]+diff
                if diff==0:
                    grades[i]=grades[i]
        else:
            grades[i]=grades[i]
    return grades

print(gradingStudents([45,56,67,74]))