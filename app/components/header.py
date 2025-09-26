import reflex as rx
from app.states.base_state import BaseState
from app.states.auth_state import AuthState


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.button(
                rx.icon("menu", class_name="w-6 h-6 text-gray-600"),
                on_click=BaseState.toggle_sidebar,
                class_name="p-2 rounded-md hover:bg-gray-100 hidden md:block",
            ),
            rx.el.button(
                rx.icon("menu", class_name="w-6 h-6 text-gray-600"),
                on_click=BaseState.toggle_drawer,
                class_name="p-2 rounded-md hover:bg-gray-100 md:hidden",
            ),
            class_name="flex items-center",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("bell", class_name="w-6 h-6 text-gray-600"),
                class_name="p-2 rounded-full hover:bg-gray-100",
            ),
            rx.el.div(
                rx.el.img(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={AuthState.current_user_email}",
                    class_name="w-9 h-9 rounded-full",
                ),
                class_name="ml-4",
            ),
            class_name="flex items-center",
        ),
        class_name="flex items-center justify-between h-16 px-4 bg-white/50 backdrop-blur-sm border-b border-gray-200 md:w-full",
    )