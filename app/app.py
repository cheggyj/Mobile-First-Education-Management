import reflex as rx
from app.pages.login import login
from app.pages.dashboard import dashboard
from app.pages.overview import overview
from app.pages.admin import admin
from app.pages.staff import staff
from app.pages.students import students
from app.states.auth_state import AuthState
from app.db import User, Student, Staff

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(login)
app.add_page(dashboard, on_load=AuthState.require_login)
app.add_page(overview, on_load=AuthState.require_login)
app.add_page(admin, on_load=AuthState.require_login)
app.add_page(staff, on_load=AuthState.require_login)
app.add_page(students, on_load=AuthState.require_login)