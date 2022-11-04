class Student:
    student_list=[]
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.student_list.append(self)

    def agrade(self, grades, a=0, b=0):
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 1)

    def rate_lc(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        course_p = ", ".join(self.courses_in_progress)
        course_f = ", ".join(self.finished_courses)
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.agrade(self.grades)}'
        f'\nКурсы в процессе изучения: {course_p}\nЗавершенные курсы: {course_f}')
        return res
    #
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return {self.agrade(self.grades)} > {other.agrade(other.grades)}

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    lecturer_list = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.lecturer_list.append(self)

    def agrade(self, grades, a=0, b=0):
        for key in grades:
            a += (len(grades[key]))
            b += (sum(grades[key]))
        return round(b / a, 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return {self.agrade(self.grades)} > {other.agrade(other.grades)}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.agrade(self.grades)}')
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res


one_student = Student('Иван', 'Петров', 'Male')
one_student.finished_courses = ['Введение в програмирование']
one_student.courses_in_progress = ['Python', 'Git']
two_student = Student('Петр', 'Сидоров', 'Male')
two_student.finished_courses = ['Введение в програмирование']
two_student.courses_in_progress = ['Python', 'Git']

one_reviewer = Reviewer('Алесандр', 'Друзь')
one_reviewer.courses_attached = ['Python', 'Git']
two_reviewer = Reviewer('Максим', 'Паташёв')
two_reviewer.courses_attached = ['Python', 'Git']

one_reviewer.rate_hw(one_student, 'Python', 10)
one_reviewer.rate_hw(one_student, 'Python', 7)
two_reviewer.rate_hw(one_student, 'Git', 9)
two_reviewer.rate_hw(one_student, 'Git', 10)
one_reviewer.rate_hw(two_student, 'Python', 7)
one_reviewer.rate_hw(two_student, 'Python', 6)
two_reviewer.rate_hw(two_student, 'Git', 8)
two_reviewer.rate_hw(two_student, 'Git', 9)
print(one_student)
print()
print(two_student)
print()

one_lecturer = Lecturer('Владислав', 'Мищенко')
one_lecturer.courses_attached = ['Python', 'Git']

two_lecturer = Lecturer('Евгений', 'Мокиевский')
two_lecturer.courses_attached = ['Python', 'Git']
one_student.rate_lc(one_lecturer, 'Git', 10)
one_student.rate_lc(two_lecturer, 'Git', 10)
two_student.rate_lc(one_lecturer, 'Python', 9)
two_student.rate_lc(two_lecturer, 'Python', 10)

print(one_lecturer)
print()
print(two_lecturer)
print()

print('Лучший стунден по средней оценке:')
if two_student.agrade(two_student.grades) > one_student.agrade(one_student.grades):
    print(f'{two_student.name} {two_student.surname} - {two_student.agrade(two_student.grades)}')
else:
    print(f'{one_student.name} {one_student.surname} - {one_student.agrade(one_student.grades)}')
print()

print('Лучший лектор по средней оценке:')
if two_lecturer.agrade(two_lecturer.grades) > one_lecturer.agrade(one_lecturer.grades):
    print(f'{two_lecturer.name} {two_lecturer.surname} - {two_lecturer.agrade(two_lecturer.grades)}')
else:
    print(f'{one_lecturer.name} {one_lecturer.surname} - {one_lecturer.agrade(one_lecturer.grades)}')
print()

def average_rating(list_stud, course, a=0, b=0):
    for instance in list_stud:
        if course in instance.grades.keys():
            a += sum(list(map(int, instance.grades[course])))
            b += len(list(map(int, instance.grades[course])))
    average = round(a / b, 1)
    return average

print(f'Средняя оценка за курс Git среди студентов: {average_rating(Student.student_list, "Git")}')
print(f'Средняя оценка за курс Git среди лекторов: {average_rating(Lecturer.lecturer_list, "Git")}')
print(f'Средняя оценка за курс Python среди студентов: {average_rating(Student.student_list, "Python")}')
print(f'Средняя оценка за курс Python среди лекторов: {average_rating(Lecturer.lecturer_list, "Python")}')




