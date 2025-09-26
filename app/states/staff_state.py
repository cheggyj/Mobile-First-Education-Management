import reflex as rx
from typing import Literal
from app.db import Staff


class StaffState(rx.State):
    staff_members: list[Staff] = []
    active_tab: Literal["teaching", "non-teaching"] = "teaching"
    show_add_staff_modal: bool = False

    @rx.var
    def filtered_staff(self) -> list[Staff]:
        return [s for s in self.staff_members if s.staff_type == self.active_tab]

    def on_load(self):
        with rx.session() as session:
            self.staff_members = session.exec(Staff.select()).all()

    def set_active_tab(self, tab: Literal["teaching", "non-teaching"]):
        self.active_tab = tab

    def toggle_add_staff_modal(self):
        self.show_add_staff_modal = not self.show_add_staff_modal

    @rx.event
    def add_staff(self, form_data: dict):
        with rx.session() as session:
            new_staff = Staff(
                name=form_data["name"],
                staff_type=form_data["staff_type"],
                role=form_data["role"],
                contact=form_data["contact"],
            )
            session.add(new_staff)
            session.commit()
            session.refresh(new_staff)
            self.staff_members.append(new_staff)
        self.show_add_staff_modal = False
        return rx.toast("Staff member added successfully!")