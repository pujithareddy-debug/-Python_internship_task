s1 = int(input("Enter marks of Student 1: "))
s2 = int(input("Enter marks of Student 2: "))
s3 = int(input("Enter marks of Student 3: "))
if s1 > s2 and s1 > s3:
    print("Student 1 has highest marks")
elif s2 > s1 and s2 > s3:
    print("Student 2 has highest marks")
else:
    print("Student 3 has highest marks")