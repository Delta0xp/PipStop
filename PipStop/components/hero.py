import reflex as rx

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "Empowering the Next Generation in Cloud, AI, Data & Automation",
                font_size="2xl",
                font_weight="bold",
                color="white",
                text_align="center"
            ),
            rx.text(
                "Mentorship, Community, and Discussions — all in one place.",
                font_size="md",
                color="#AAAAAA",
                text_align="center"
            ),
            rx.hstack(
                rx.button(
                    "Join Community",
                    color_scheme="pink",
                    size="3",
                    border_radius="0"
                ),
                rx.button(
                    "Become Member",
                    color_scheme="cyan",
                    size="3",
                    border_radius="0"
                ),
                spacing="0",
                padding_top="1rem",
                padding_left="6rem"
            ),
            spacing="3"
        ),
        padding_top="4rem",
        padding_bottom="4rem"
    )
