import reflex as rx
from PipStop.components.navbar import navbar

def home() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.center(
                rx.vstack(
                    rx.text(
                        "Empowering the Next Generation in Cloud, AI, Data & Automation",
                        font_size="xl",
                        font_weight="bold",
                        color="white",
                        text_align="center"
                    ),
                    rx.text(
                        "Mentorship, Community, and Discussions — all in one place.",
                        font_size="md",
                        color="#AAAAAA"
                    ),
                    rx.hstack(
                        rx.button("Join the Community", color_scheme="pink", size="3"),
                        rx.button("Become a Mentor", color_scheme="cyan", size="3"),
                        spacing="4",
                        padding_top="1rem"
                    ),
                    spacing="3"
                ),
                padding_top="4rem",
                padding_bottom="4rem"
            ),
            rx.center(
                rx.text("© 2025 Centre of Excellence • Built with Reflex", color="#888888", font_size="sm"),
                padding="1rem"
            ),
            spacing="4",
            align="stretch"
        ),
        background_color="#111111",
        min_height="100vh",
        padding="0"
    )
