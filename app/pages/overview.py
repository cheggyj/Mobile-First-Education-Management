import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.states.auth_state import AuthState


def overview_content() -> rx.Component:
    return rx.el.div(
        rx.el.h1("School Overview", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.el.p(
                "Charts and key performance indicators will be displayed here.",
                class_name="text-gray-500",
            ),
            class_name="bg-white p-6 rounded-lg border border-gray-200",
        ),
    )


@rx.page(route="/overview")
def overview() -> rx.Component:
    return dashboard_layout(overview_content())