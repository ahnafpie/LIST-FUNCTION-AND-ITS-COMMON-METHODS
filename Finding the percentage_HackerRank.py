"""
problem: You have a  record of N students.  Each record  contains  the student's name, and their percent marks in Maths,
Physics  and  Chemistry.  The  marks  can be floating  values. The user enters some  integer N followed by the names and
marks for N students. You are required to save the record in  a dictionary  data type.  The user then enters a student's
name. Output the average percentage marks obtained by that student, correct to two decimal places.

SAMPLE INPUT:
2
Harsh 25 26.5 28
Andra 26 28 30
Harsh

SAMPLE OUTPUT: Average marks of Harsh
26.50
"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(sum(student_marks[query_name]) / len(student_marks[query_name])))
