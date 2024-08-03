from students import insert_students, recover_student, populate_table

# Populando a tabela com 10 registros
populate_table()

# Exemplo de uso: Recuperar student com ID 5
student_id = 6
student = recover_student(student_id)
if student:
    print(f"Aluno encontrado: ID={student['id']}, Nome={student['name']}, Idade={student['age']}")
else:
    print(f"Aluno com ID {student_id} não encontrado.")