from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import random

Base = declarative_base()
association_table = Table(
    'association_table', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship("Student", secondary=association_table, back_populates="courses")


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    courses = relationship("Course", secondary=association_table, back_populates="students")


engine = create_engine("sqlite:///example.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

all_courses = [
    Course(name="History"),
    Course(name="Chemistry"),
    Course(name="Programming"),
    Course(name="Mathematics")
]
all_students = [
    Student(name='John', age=30, courses=random.sample(all_courses, 1)),
    Student(name='Vitalii', age=35, courses=random.sample(all_courses, 2)),
    Student(name='Andrew', age=33, courses=random.sample(all_courses, 3))
]


def print_all_students():
    print("Print all students:")
    for student in session.query(Student).all():
        course_names = ", ".join(course.name for course in student.courses)
        print(f"Student: {student.name}, Age: {student.age}, Courses: {course_names}")


def add_new_student(name, age, courses):
    course_names = ", ".join(course.name for course in courses)
    student = Student(name=name, age=age, courses=courses)
    print(f"Adding new Student: {student.name}, Age: {student.age}, Courses: {course_names}")
    session.add(student)
    session.commit()


def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student {name} deleted.")


def get_student_by_name(name):
    return session.query(Student).filter_by(name=name).first()


def update_student(name, age, courses):
    student = session.query(Student).filter_by(name=name).first()
    print("updating student")
    if student:
        print("Student = ", student)
        student.age = age
        student.courses = courses
        session.commit()


try:
    session.begin()
    session.add_all(all_courses)
    session.commit()
    session.add_all(all_students)
    session.commit()
    add_new_student("William", 45, courses=random.sample(all_courses, 3))
    update_student("John", 31, courses=random.sample(all_courses, 3))
    delete_student("Andrew")
    print_all_students()
except Exception as e:
    session.rollback()
    print(f" Exception occurred: {e}")
finally:
    session.close()
