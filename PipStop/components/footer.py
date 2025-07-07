import reflex as rx

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("© 2025 Centre of Excellence •", color="#FFFFFF", font_size="sm"),
            rx.hstack(
                rx.link("Twitter", href="https://twitter.com", color="#AAAAAA"),
                rx.link("LinkedIn", href="https://linkedin.com", color="#AAAAAA"),
                rx.link("GitHub", href="https://github.com", color="#AAAAAA"),
                spacing="4",
                # margin_left="3rem"
            ),
            spacing="2",
            # margin_left="1rem"
        ),
        # padding="2rem"
    )
