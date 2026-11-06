# print("Hello!")

student_name = input()

Math_mark = 85
English_mark = 75
Python_mark = 90

A = (Math_mark + English_mark + Python_mark) / 3
print(A)

if A>= 80 :
    grade = "A+"

else :
    grade = "F"

print(f"studet_name {student_name}")
print(f"Avg_mark {A}")
print(f"final grade {grade}")
