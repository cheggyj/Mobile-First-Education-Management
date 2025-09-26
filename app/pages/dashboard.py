import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.components.stat_card import stat_card
from app.states.base_state import BaseState
from app.states.auth_state import AuthState


def dashboard_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("Dashboard", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.foreach(BaseState.stats, stat_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6",
        ),
        rx.el.div(
            rx.el.h2(
                "Recent Activity",
                class_name="text-xl font-bold text-gray-900 mt-8 mb-4",
            ),
            rx.el.div(
                rx.el.p("No recent activity to display.", class_name="text-gray-500"),
                class_name="bg-white p-6 rounded-lg border border-gray-200",
            ),
        ),
    )


@rx.page(route="/")
def dashboard() -> rx.Component:
    return dashboard_layout(dashboard_page())