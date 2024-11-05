class Student:
    def __init__(self, first_name: str, last_name: str, age: int, avg_score: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_score = avg_score

    def set_score(self, score: int):
        self.avg_score = score



piotr_student = Student("Piotr", "Czapik", 22, 98)
piotr_student.set_score(100)

print(f"""
Student: 
First Name={piotr_student.first_name}, Last Name={piotr_student.last_name}
Age ={piotr_student.age}, Average score={piotr_student.avg_score}
""")
