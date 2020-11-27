"""
input: names and grades; N students
store them in a nested list

print name(s) of any student(s) with second lowest grade
"""

def get_lowest_score_students(nested_list):
    second_highest = sorted(set([score for name, score in nested_list]))[1]
    sorted_list = sorted([name for name, score in nested_list if score == second_highest])
    print('\n'.join(sorted_list))



if __name__ == '__main__':
    # nested_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        nested_list.append([name, score])
    
    get_lowest_score_students(nested_list)