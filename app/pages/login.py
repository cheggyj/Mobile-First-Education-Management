import reflex as rx
from app.components.login_card import login_card


def login() -> rx.Component:
    return rx.el.div(
        login_card(),
        class_name="flex min-h-screen items-center justify-center bg-gray-50 font-['Inter'] px-4",
    )