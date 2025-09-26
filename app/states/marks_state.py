import reflex as rx
from app.db import Mark


class MarksState(rx.State):
    marks: list[Mark] = []

    def on_load(self):
        with rx.session() as session:
            self.marks = session.exec(Mark.select()).all()