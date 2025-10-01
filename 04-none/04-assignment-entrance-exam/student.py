
# average must be at least 12


def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    truthy_grades = []
    for i in [grade1, grade2, grade3, grade4, grade5]:
        if i is not None:
            truthy_grades.append(i)

    if len(truthy_grades) <= 3:
        return False

    average_grades = sum(truthy_grades) / len(truthy_grades)

    if average_grades < 12:
        return False
    return True
