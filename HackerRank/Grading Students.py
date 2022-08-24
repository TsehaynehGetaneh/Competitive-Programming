def gradingStudents(grades):
    result= []
    for grade in grades:
        if grade >= 38:
            modulus5 = grade % 5
            if modulus5 >=3:
                grade = (grade - modulus5) + 5
                result.append(grade)
            else:
                result.append(grade)
        else:
            result.append(grade)
    return result