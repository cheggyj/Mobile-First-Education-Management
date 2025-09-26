import reflex as rx
from typing import TypedDict


class StatCardData(TypedDict):
    title: str
    value: str
    icon: str
    color: str


class BaseState(rx.State):
    sidebar_open: bool = True
    drawer_open: bool = False
    stats: list[StatCardData] = [
        {
            "title": "Total Students",
            "value": "1,204",
            "icon": "users",
            "color": "bg-emerald-500",
        },
        {
            "title": "Total Staff",
            "value": "86",
            "icon": "briefcase",
            "color": "bg-blue-500",
        },
        {
            "title": "Attendance Rate",
            "value": "92.5%",
            "icon": "check-circle",
            "color": "bg-yellow-500",
        },
        {
            "title": "Recent Activities",
            "value": "12",
            "icon": "activity",
            "color": "bg-pink-500",
        },
    ]

    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    def toggle_drawer(self):
        self.drawer_open = not self.drawer_open