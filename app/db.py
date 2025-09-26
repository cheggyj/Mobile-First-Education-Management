import reflex as rx


class User(rx.Model, table=True):
    email: str
    password: str
    role: str


class Student(rx.Model, table=True):
    name: str
    grade: str
    parent_guardian_details: str
    medical_information: str


class Staff(rx.Model, table=True):
    name: str
    staff_type: str
    role: str
    contact: str


class Mark(rx.Model, table=True):
    student_id: int
    subject: str
    score: float
    term: str