import reflex as rx
from app.states.base_state import BaseState
from app.states.auth_state import AuthState


def nav_item(text: str, href: str, icon: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5"),
        rx.el.span(
            text,
            class_name=rx.cond(BaseState.sidebar_open, "opacity-100", "opacity-0 w-0"),
        ),
        href=href,
        class_name="flex items-center gap-3 px-4 py-2.5 rounded-md text-gray-700 hover:bg-emerald-50 hover:text-emerald-600 transition-colors duration-200",
    )


def sidebar() -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("graduation-cap", class_name="w-8 h-8 text-emerald-600"),
                rx.el.h1(
                    "Academia",
                    class_name=rx.cond(
                        BaseState.sidebar_open,
                        "font-bold text-2xl text-gray-800 opacity-100",
                        "opacity-0 w-0",
                    ),
                ),
                class_name="flex items-center gap-3 p-4",
            ),
            rx.el.nav(
                nav_item("Dashboard", "/", "layout-dashboard"),
                nav_item("Overview", "/overview", "bar-chart-3"),
                rx.cond(
                    AuthState.is_admin,
                    rx.fragment(
                        nav_item("Admin Overview", "/admin", "shield"),
                        nav_item("Staff", "/staff", "users"),
                        nav_item("Students", "/students", "user-round"),
                    ),
                ),
                rx.cond(
                    AuthState.is_teacher | AuthState.is_student | AuthState.is_parent,
                    nav_item("Marks", "/marks", "graduation-cap"),
                ),
                class_name="flex flex-col gap-1 p-2",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.a(
                rx.icon("log-out", class_name="w-5 h-5"),
                rx.el.span(
                    "Logout",
                    class_name=rx.cond(
                        BaseState.sidebar_open, "opacity-100", "opacity-0 w-0"
                    ),
                ),
                on_click=AuthState.logout,
                class_name="flex items-center gap-3 px-4 py-2.5 rounded-md text-gray-700 hover:bg-red-50 hover:text-red-600 transition-colors duration-200 cursor-pointer",
            ),
            class_name="p-2 border-t border-gray-200",
        ),
        class_name=rx.cond(
            BaseState.sidebar_open,
            "w-64 bg-gray-50/50 border-r border-gray-200 flex-col transition-all duration-300 hidden md:flex",
            "w-20 bg-gray-50/50 border-r border-gray-200 flex-col transition-all duration-300 hidden md:flex",
        ),
    )