import reflex as rx
from app.db import Student


class StudentState(rx.State):
    students: list[Student] = []
    show_add_student_modal: bool = False

    def on_load(self):
        with rx.session() as session:
            self.students = session.exec(Student.select()).all()

    def toggle_add_student_modal(self):
        self.show_add_student_modal = not self.show_add_student_modal

    @rx.event
    def add_student(self, form_data: dict):
        with rx.session() as session:
            new_student = Student(
                name=form_data["name"],
                grade=form_data["grade"],
                parent_guardian_details=form_data["parent_details"],
                medical_information=form_data["medical_info"],
            )
            session.add(new_student)
            session.commit()
            session.refresh(new_student)
            self.students.append(new_student)
        self.show_add_student_modal = False
        return rx.toast("Student added successfully!")