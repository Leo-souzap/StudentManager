class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class StudentTable:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def recover_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

# Populando a tabela com 10 registros
def populate_table(table):
    for i in range(1, 11):
        table.add_student(Student(i, f"Aluno {i}", 20 + i))
