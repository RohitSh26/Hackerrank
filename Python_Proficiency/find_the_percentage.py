"""
The provided code stub will read in a dictionary containing key/value pairs of 
name:[marks] 
for a list of students.

Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
from functools import reduce

def find_avaerage(scores):
    average = reduce(lambda x, y: x + y, scores) / len(scores)
    print("{:.2f}".format(average))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # scores = [1, 2, 3]
    find_avaerage(student_marks[query_name])