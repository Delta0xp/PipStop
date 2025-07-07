import reflex as rx

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("© 2025 Centre of Excellence • Built with Reflex", color="#888888", font_size="sm"),
            rx.hstack(
                rx.link("Twitter", href="https://twitter.com", color="#AAAAAA"),
                rx.link("LinkedIn", href="https://linkedin.com", color="#AAAAAA"),
                rx.link("GitHub", href="https://github.com", color="#AAAAAA"),
                spacing="4"
            ),
            spacing="2"
        ),
        padding="2rem"
    )
