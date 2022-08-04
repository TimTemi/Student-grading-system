import random, tabulate, os
from datetime import date

def read_names(fileObject):
    names = fileObject.readlines()
    names = [i.replace('\n', '') for i in names]
    return names


def get_random_student(first_names, last_names):
    genders = ['male', 'female']
    randn = random.randint(0, 1)
    first_names = first_names[genders[randn]]
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    student = {'name':f'{first_name} {last_name}', 'gender':genders[randn].upper(), 'year':date.today().year}
    return student


def get_remark(gpa):
    if gpa >=4 and gpa <= 5:
        return 'VERY GOOD'
    elif gpa >=3 and gpa < 4:
        return 'GOOD'
    elif gpa >=2.5 and gpa < 3:
        return 'FAIR'
    elif gpa < 2.5:
        return 'POOR'


def compile_grade(student, courses, course_units, grade_letters):
    grades = []
    headers = ['COURSE', 'GRADE', 'CREDIT UNIT']
    credit_load = sum(course_units)

    grade_numbers = [i for i in reversed(range(0, 6))]
    grade_letter2num = {k:v for k,v in zip(grade_letters, grade_numbers)}
    remark = ''
    gpa = 0

    for idx, course in enumerate(courses):
        grade_letter = random.choice(grade_letters)
        grade_point = grade_letter2num[grade_letter]
        gpa += grade_point * course_units[idx]
        grades.append(grade_letter)

    gpa = gpa / credit_load
    
    result = tabulate.tabulate(zip(courses, grades, course_units), tablefmt='rst', headers=headers)
    output = 'NAME: {name}'.format(name=student['name'])
    output += '\n\nGENDER: {gender}'.format(gender=student['gender'])
    output += '\n\nYEAR: {year}'.format(year=student['year'])
    output += f'\n\n{result}'
    output += f'\n\nTOTAL CREDIT LOAD: \t{credit_load}'
    output += f'\n\nGPA: {gpa}'
    output += f'\n\nREMARK: {get_remark(gpa)}'
    return output


if __name__ == '__main__':
    
    name_folder = 'names'
    result_folder = 'student_results'

    male_names_file = os.path.join(name_folder, 'male-first-names.txt')
    female_names_file = os.path.join(name_folder, 'female-first-names-1.txt')
    last_names_file = os.path.join(name_folder, 'last-names.txt')

    male_names = read_names(open(male_names_file, 'r'))
    female_names = read_names(open(female_names_file, 'r'))
    last_names = read_names(open(last_names_file, 'r'))
    first_names = {'male':male_names, 'female':female_names}


    student = get_random_student(first_names, last_names)

    courses = ['MAT112', 'CPE123', 'GST104', 'MAT221', 'CPI109', 'CPT342', 'EET124', 'AET214']
    course_units = [3 for i in range(len(courses))]
    grade_letters = [chr(ord('A')+i) for i in range(0, 6)]

    student_result = compile_grade(student, courses, course_units, grade_letters)
    
    result_file = os.path.join(result_folder, "{student_name}.txt".format(student_name=student['name'].lower()))
    with open(result_file, 'w') as f:
        f.write(student_result)
    f.close()