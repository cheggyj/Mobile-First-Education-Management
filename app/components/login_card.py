import reflex as rx
from app.states.auth_state import AuthState


def login_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("graduation-cap", class_name="w-10 h-10 text-emerald-600"),
            rx.el.h2(
                "Academia Portal", class_name="text-2xl font-bold mt-2 text-gray-900"
            ),
            class_name="flex flex-col items-center mb-6",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Email",
                    html_for="email",
                    class_name="text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    type="email",
                    id="email",
                    name="email",
                    placeholder="admin@school.com",
                    class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md text-sm h-10 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Password",
                    html_for="password",
                    class_name="text-sm font-medium text-gray-700",
                ),
                rx.el.input(
                    type="password",
                    id="password",
                    name="password",
                    placeholder="password",
                    class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md text-sm h-10 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        type="checkbox",
                        id="remember",
                        name="remember",
                        class_name="h-4 w-4 text-emerald-600 border-gray-300 rounded focus:ring-emerald-500",
                    ),
                    rx.el.label(
                        "Remember me",
                        html_for="remember",
                        class_name="ml-2 block text-sm text-gray-900",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.a(
                    "Forgot password?",
                    href="#",
                    class_name="text-sm text-emerald-600 hover:text-emerald-500",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.cond(
                AuthState.error_message != "",
                rx.el.div(
                    AuthState.error_message,
                    class_name="text-red-500 text-sm mb-4 p-2 bg-red-50 border border-red-200 rounded-md",
                ),
                rx.el.div(),
            ),
            rx.el.button(
                "Sign In",
                type="submit",
                class_name="w-full flex justify-center py-2.5 px-4 border border-transparent rounded-md text-sm font-medium text-white bg-emerald-600 h-10 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500",
            ),
            on_submit=AuthState.login,
        ),
        rx.el.div(
            rx.el.div(class_name="flex-grow border-t border-gray-300"),
            rx.el.span(
                "or continue with", class_name="flex-shrink mx-4 text-sm text-gray-500"
            ),
            rx.el.div(class_name="flex-grow border-t border-gray-300"),
            class_name="relative flex justify-center items-center my-6",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon("github", class_name="w-5 h-5"),
                class_name="flex-1 justify-center inline-flex items-center py-2 px-4 border border-gray-300 rounded-md bg-white text-sm font-medium text-gray-500 h-10 hover:bg-gray-50",
            ),
            rx.el.button(
                rx.icon("gitlab", class_name="w-5 h-5"),
                class_name="flex-1 justify-center inline-flex items-center py-2 px-4 border border-gray-300 rounded-md bg-white text-sm font-medium text-gray-500 h-10 hover:bg-gray-50",
            ),
            class_name="flex gap-4",
        ),
        class_name="w-full max-w-sm p-8 bg-white border border-gray-200 rounded-lg",
    )