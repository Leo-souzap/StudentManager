from students import Student, StudentTable, populate_table

if __name__ == "__main__":
    table = StudentTable()
    populate_table(table)
    student = table.recover_student_by_id(11)
    if student:
        print(f"Aluno encontrado: {student.name}, Idade: {student.age}")
    else:
        print("Aluno não encontrado")