import reflex as rx


def bottom_nav_item(text: str, href: str, icon: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, class_name="w-6 h-6 mb-1"),
        rx.el.span(text, class_name="text-xs font-medium"),
        href=href,
        class_name="flex flex-col items-center justify-center flex-1 text-gray-600 hover:text-emerald-600",
    )


def bottom_nav() -> rx.Component:
    return rx.el.div(
        bottom_nav_item("Dashboard", "/", "layout-dashboard"),
        bottom_nav_item("Overview", "/overview", "bar-chart-3"),
        bottom_nav_item("Staff", "/staff", "users"),
        bottom_nav_item("Students", "/students", "user-round"),
        class_name="fixed bottom-0 left-0 right-0 h-16 bg-white border-t border-gray-200 flex md:hidden z-40",
    )