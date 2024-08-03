students = []

def insert_students(id, name, age):
    student = {
        'id': id,
        'name': name,
        'age': age
    }
    students.append(student)

def recover_student(id):
    for student in students:
        if student['id'] == id:
            return student
    return None

def populate_table():
    insert_students(1, 'Leo', 20)
    insert_students(2, 'Rodrigo', 21)
    insert_students(3, 'Giovanna', 22)
    insert_students(4, 'Cristiane', 23)
    insert_students(5, 'Glauco', 24)
    insert_students(6, 'Claudia', 25)
    insert_students(7, 'Carine', 26)
    insert_students(8, 'Alexandre', 27)
    insert_students(9, 'Caique', 28)
    insert_students(10, 'Claudio', 29)