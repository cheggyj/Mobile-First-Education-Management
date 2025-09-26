import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.components.student.add_student_modal import add_student_modal
from app.states.student_state import StudentState
from app.states.auth_state import AuthState


def students_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Student Management", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.button(
                rx.icon("plus", class_name="mr-2 w-4 h-4"),
                "Add New Student",
                on_click=StudentState.toggle_add_student_modal,
                class_name="flex items-center px-4 py-2 bg-emerald-600 text-white rounded-md h-10 hover:bg-emerald-700",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Grade",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Parent/Guardian",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        StudentState.students,
                        lambda student: rx.el.tr(
                            rx.el.td(
                                student.name,
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                student.grade,
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                student.parent_guardian_details,
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            class_name="hover:bg-gray-50",
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white border border-gray-200 rounded-lg overflow-hidden mt-6",
        ),
        add_student_modal(),
        on_mount=StudentState.on_load,
    )


@rx.page(route="/students")
def students() -> rx.Component:
    return dashboard_layout(students_content())