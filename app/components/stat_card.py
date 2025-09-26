import reflex as rx


def stat_card(data: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(data["icon"], class_name="w-6 h-6 text-white"),
            class_name=f"p-3 rounded-full {data['color']}",
        ),
        rx.el.p(data["title"], class_name="text-sm font-medium text-gray-500 mt-4"),
        rx.el.p(data["value"], class_name="text-2xl font-bold text-gray-900"),
        class_name="bg-white p-6 rounded-lg border border-gray-200",
    )