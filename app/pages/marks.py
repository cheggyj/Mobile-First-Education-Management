import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.marks_state import MarksState


def marks_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Marks Overview", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.el.p(
                "Student marks and performance data will be displayed here.",
                class_name="text-gray-500",
            ),
            class_name="bg-white p-6 rounded-lg border border-gray-200",
        ),
        on_mount=MarksState.on_load,
    )


@rx.page(route="/marks")
def marks() -> rx.Component:
    return dashboard_layout(marks_content())