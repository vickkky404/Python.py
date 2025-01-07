# program to create a grading system
# 90 and above: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F

g = float(input("Enter your percentage.."))

if g >= 90:
    print("A")
elif g >= 80:
    print("Grade B")
elif g >= 70:
    print("C")
elif g >= 60:
    print("D")
elif g <= 60:
    print("F")
