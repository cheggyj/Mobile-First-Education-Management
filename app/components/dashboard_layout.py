import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.components.bottom_nav import bottom_nav
from app.components.drawer import drawer
from app.states.auth_state import AuthState


def dashboard_layout(child: rx.Component) -> rx.Component:
    return rx.el.div(
        sidebar(),
        drawer(),
        rx.el.div(
            header(),
            rx.el.main(
                child, class_name="p-4 md:p-6 lg:p-8 overflow-y-auto pb-20 md:pb-0"
            ),
            class_name="flex-1 flex flex-col h-screen md:w-full",
        ),
        bottom_nav(),
        on_mount=AuthState.on_load,
        class_name="flex font-['Inter'] bg-gray-50 text-gray-900 min-h-screen",
    )