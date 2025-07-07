import reflex as rx

def testimonials() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("What Our Members Say", font_size="xl", font_weight="bold", color="white"),
            rx.hstack(
                rx.box(
                    rx.text("“An inspiring community that pushes me to be my best!”", color="#AAAAAA", font_style="italic"),
                    rx.text("— Khabho, Data Engineer", color="white", margin_top="0.5rem"),
                    padding="1rem",
                    background_color="#1a1a1a",
                    border_radius="xl",
                    width="250px"
                ),
                rx.box(
                    rx.text("“The mentorship here accelerated my career like nothing else.”", color="#AAAAAA", font_style="italic"),
                    rx.text("— Tio, AI Scientist", color="white", margin_top="0.5rem"),
                    padding="1rem",
                    background_color="#1a1a1a",
                    border_radius="xl",
                    width="250px"
                ),
                rx.box(
                    rx.text("“I finally found my tribe. Knowledge-sharing at its finest!”", color="#AAAAAA", font_style="italic"),
                    rx.text("— Ryan, Cloud Architect", color="white", margin_top="0.5rem"),
                    padding="1rem",
                    background_color="#1a1a1a",
                    border_radius="xl",
                    width="250px"
                ),
                spacing="5"
            ),
            spacing="4"
        ),
        padding_top="4rem",
        padding_bottom="4rem"
    )
