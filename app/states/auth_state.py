import reflex as rx
from typing import Optional
from app.db import User, Student, Staff, Mark


class AuthState(rx.State):
    user: Optional[User] = None
    error_message: str = ""

    @rx.var
    def is_authenticated(self) -> bool:
        return self.user is not None

    def _create_default_user(self):
        with rx.session() as session:
            rx.Model.create_all()
            existing_user = session.exec(
                User.select().where(User.email == "admin@school.com")
            ).first()
            if not existing_user:
                new_user = User(
                    email="admin@school.com", password="password", role="super_admin"
                )
                session.add(new_user)
                session.commit()

    @rx.event
    def on_load(self):
        self._create_default_user()
        if self.is_authenticated:
            pass
        return

    @rx.event
    def login(self, form_data: dict):
        email = form_data["email"]
        password = form_data["password"]
        with rx.session() as session:
            user = session.exec(User.select().where(User.email == email)).first()
            if user and user.password == password:
                self.user = user
                self.error_message = ""
                return rx.redirect("/")
            else:
                self.error_message = "Invalid email or password."
                self.user = None

    @rx.event
    def logout(self):
        self.user = None
        return rx.redirect("/login")

    @rx.var
    def current_user_email(self) -> str:
        return self.user.email if self.user else ""

    @rx.var
    def current_user_role(self) -> str:
        return self.user.role if self.user else ""

    @rx.var
    def is_super_admin(self) -> bool:
        return self.current_user_role == "super_admin"

    @rx.var
    def is_admin(self) -> bool:
        return self.current_user_role in ["admin", "super_admin"]

    @rx.var
    def is_teacher(self) -> bool:
        return self.current_user_role == "teacher"

    @rx.var
    def is_student(self) -> bool:
        return self.current_user_role == "student"

    @rx.var
    def is_parent(self) -> bool:
        return self.current_user_role == "parent"

    def require_login(self):
        if not self.is_authenticated:
            return rx.redirect("/login")

    def require_admin_privileges(self):
        if not self.is_authenticated:
            return rx.redirect("/login")
        if not self.is_admin:
            return rx.redirect("/")