import unittest
from src.students import Student, StudentTable, populate_table

class StudentsManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.table = StudentTable()
        populate_table(self.table)

    def test_add_student(self):
        student = Student(11, "Aluno 10", 30)
        self.table.add_student(student)
        self.assertEqual(len(self.table.students), 11)
        self.assertEqual(self.table.students[-1].name, "Aluno 10")

    def test_recover_student_by_id(self):
        student = self.table.recover_student_by_id(1)
        self.assertIsNotNone(student)
        self.assertEqual(student.name, "Aluno 1")

    def test_recover_student_by_id_nao_existente(self):
        student = self.table.recover_student_by_id(999)
        self.assertIsNone(student)

if __name__ == '__main__':
    unittest.main()