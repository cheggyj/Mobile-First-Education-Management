import reflex as rx
from app.states.student_state import StudentState


def add_student_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.form(
                rx.el.div(
                    rx.el.h3(
                        "Add New Student",
                        class_name="text-lg font-medium text-gray-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="w-5 h-5"),
                        on_click=StudentState.toggle_add_student_modal,
                        class_name="p-1 rounded-full hover:bg-gray-100",
                    ),
                    class_name="flex justify-between items-center pb-4 border-b border-gray-200",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Full Name", class_name="text-sm font-medium text-gray-700"
                        ),
                        rx.el.input(
                            name="name",
                            placeholder="Jane Smith",
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-md h-10 focus:outline-none focus:border-emerald-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Grade / Class",
                            class_name="text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="grade",
                            placeholder="Grade 8",
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-md h-10 focus:outline-none focus:border-emerald-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Parent/Guardian Details",
                            class_name="text-sm font-medium text-gray-700",
                        ),
                        rx.el.input(
                            name="parent_details",
                            placeholder="parent@example.com",
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-md h-10 focus:outline-none focus:border-emerald-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Medical Information",
                            class_name="text-sm font-medium text-gray-700",
                        ),
                        rx.el.textarea(
                            name="medical_info",
                            placeholder="e.g. Allergies, conditions",
                            class_name="w-full mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:border-emerald-500",
                        ),
                    ),
                    class_name="py-4",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancel",
                        type="button",
                        on_click=StudentState.toggle_add_student_modal,
                        class_name="px-4 py-2 bg-gray-100 text-gray-700 rounded-md h-10 hover:bg-gray-200",
                    ),
                    rx.el.button(
                        "Add Student",
                        type="submit",
                        class_name="px-4 py-2 bg-emerald-600 text-white rounded-md h-10 hover:bg-emerald-700",
                    ),
                    class_name="flex justify-end gap-3 pt-4 border-t border-gray-200",
                ),
                on_submit=StudentState.add_student,
                reset_on_submit=True,
            ),
            class_name="bg-white rounded-lg p-6 w-full max-w-lg",
        ),
        open=StudentState.show_add_student_modal,
        class_name="fixed inset-0 z-50 open:flex items-center justify-center bg-black/50 backdrop-blur-sm",
    )