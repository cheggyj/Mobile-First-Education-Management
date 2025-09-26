import reflex as rx
from app.components.dashboard_layout import dashboard_layout
from app.components.staff.add_staff_modal import add_staff_modal
from app.states.staff_state import StaffState
from app.states.auth_state import AuthState


def staff_content() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1("Staff Management", class_name="text-2xl font-bold text-gray-900"),
            rx.el.button(
                rx.icon("plus", class_name="mr-2 w-4 h-4"),
                "Add New Staff",
                on_click=StaffState.toggle_add_staff_modal,
                class_name="flex items-center px-4 py-2 bg-emerald-600 text-white rounded-md h-10 hover:bg-emerald-700",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.button(
                "Teaching Staff",
                on_click=lambda: StaffState.set_active_tab("teaching"),
                class_name=rx.cond(
                    StaffState.active_tab == "teaching",
                    "px-4 py-2 font-medium border-b-2 border-emerald-500 text-emerald-600",
                    "px-4 py-2 font-medium text-gray-500 hover:text-gray-700",
                ),
            ),
            rx.el.button(
                "Non-Teaching Staff",
                on_click=lambda: StaffState.set_active_tab("non-teaching"),
                class_name=rx.cond(
                    StaffState.active_tab == "non-teaching",
                    "px-4 py-2 font-medium border-b-2 border-emerald-500 text-emerald-600",
                    "px-4 py-2 font-medium text-gray-500 hover:text-gray-700",
                ),
            ),
            class_name="flex border-b border-gray-200",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Name",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Role",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                        rx.el.th(
                            "Contact",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        StaffState.filtered_staff,
                        lambda staff: rx.el.tr(
                            rx.el.td(
                                staff.name,
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                staff.role,
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                staff.contact,
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            class_name="hover:bg-gray-50",
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200",
            ),
            class_name="bg-white border border-gray-200 rounded-lg overflow-hidden mt-6",
        ),
        add_staff_modal(),
        on_mount=StaffState.on_load,
    )


@rx.page(route="/staff")
def staff() -> rx.Component:
    return dashboard_layout(staff_content())