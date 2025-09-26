import reflex as rx
from app.states.base_state import BaseState
from app.states.auth_state import AuthState


def drawer_nav_item(text: str, href: str, icon: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-5 h-5"),
        rx.el.span(text),
        href=href,
        class_name="flex items-center gap-3 px-4 py-2.5 rounded-md text-gray-700 hover:bg-emerald-50 hover:text-emerald-600 transition-colors duration-200",
    )


def drawer() -> rx.Component:
    return rx.el.div(
        rx.cond(
            BaseState.drawer_open,
            rx.el.div(
                on_click=BaseState.toggle_drawer,
                class_name="fixed inset-0 bg-black/50 z-40 md:hidden",
            ),
        ),
        rx.el.aside(
            rx.el.div(
                rx.el.div(
                    rx.icon("graduation-cap", class_name="w-8 h-8 text-emerald-600"),
                    rx.el.h1("Academia", class_name="font-bold text-2xl text-gray-800"),
                    class_name="flex items-center gap-3 p-4 border-b border-gray-200",
                ),
                rx.el.nav(
                    drawer_nav_item("Dashboard", "/", "layout-dashboard"),
                    drawer_nav_item("Overview", "/overview", "bar-chart-3"),
                    rx.cond(
                        AuthState.is_admin,
                        rx.fragment(
                            drawer_nav_item("Admin Overview", "/admin", "shield"),
                            drawer_nav_item("Staff", "/staff", "users"),
                            drawer_nav_item("Students", "/students", "user-round"),
                        ),
                    ),
                    rx.cond(
                        AuthState.is_teacher
                        | AuthState.is_student
                        | AuthState.is_parent,
                        drawer_nav_item("Marks", "/marks", "graduation-cap"),
                    ),
                    class_name="flex flex-col gap-1 p-2",
                    on_click=BaseState.toggle_drawer,
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("log-out", class_name="w-5 h-5"),
                    rx.el.span("Logout"),
                    on_click=[AuthState.logout, BaseState.toggle_drawer],
                    class_name="flex items-center gap-3 px-4 py-2.5 rounded-md text-gray-700 hover:bg-red-50 hover:text-red-600 transition-colors duration-200 cursor-pointer",
                ),
                class_name="p-2 border-t border-gray-200",
            ),
            class_name=rx.cond(
                BaseState.drawer_open,
                "fixed top-0 left-0 h-full w-64 bg-gray-50 z-50 transform translate-x-0 transition-transform duration-300 ease-in-out",
                "fixed top-0 left-0 h-full w-64 bg-gray-50 z-50 transform -translate-x-full transition-transform duration-300 ease-in-out",
            ),
        ),
    )