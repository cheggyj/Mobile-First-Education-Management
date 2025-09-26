import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.states.auth_state import AuthState


def dashboard_layout(child: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header(),
            rx.el.main(child, class_name="p-4 md:p-6 lg:p-8 overflow-y-auto"),
            class_name="flex-1 flex flex-col h-screen",
        ),
        on_mount=AuthState.on_load,
        class_name="flex font-['Inter'] bg-gray-50 text-gray-900 min-h-screen",
    )