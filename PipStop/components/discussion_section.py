import reflex as rx

def discussion_section() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Discuss like eggs", font_size="2xl", color="white"),
            rx.text(
                "Join our mentorship program to connect with industry experts.",
                color="#AAAAAA",
                text_align="center"
            ),
            rx.button(
                "Apply Now",
                color_scheme="red",
                size="3",
                margin_top="1rem",
                border_radius="0"
            ),
            spacing="3"
        ),
        padding="4rem",
        # background_color="#FF0BAE",
        min_height="100vh"
    )
