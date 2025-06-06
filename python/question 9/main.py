# Calculate average marks of a student.
n = int(input())
student_marks = {input().split()[0]: list(map(float, input().split()))
for _ in range(n)}
query = input()
print(f"{sum(student_marks[query])/len(student_marks[query]):.2f}")

