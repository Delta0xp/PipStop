import reflex as rx

def features() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("Why Join Us?", font_size="xl", font_weight="bold", color="white"),
            rx.hstack(
                rx.box(
                    rx.text("💡", font_size="3xl"),
                    rx.text("Expert Mentorship", font_weight="semibold", color="white"),
                    rx.text("Learn directly from experienced professionals.", color="#AAAAAA"),
                    padding="1rem",
                    background_color="#222222",
                    border_radius="xl",
                    width="200px",
                    text_align="center"
                ),
                rx.box(
                    rx.text("🤝", font_size="3xl"),
                    rx.text("Vibrant Community", font_weight="semibold", color="white"),
                    rx.text("Connect and grow with like-minded peers.", color="#AAAAAA"),
                    padding="1rem",
                    background_color="#222222",
                    border_radius="xl",
                    width="200px",
                    text_align="center"
                ),
                rx.box(
                    rx.text("🚀", font_size="3xl"),
                    rx.text("Career Growth", font_weight="semibold", color="white"),
                    rx.text("Access opportunities and stay ahead.", color="#AAAAAA"),
                    padding="1rem",
                    background_color="#222222",
                    border_radius="xl",
                    width="200px",
                    text_align="center"
                ),
                spacing="5"
            ),
            spacing="4"
        ),
        padding_top="4rem",
        padding_bottom="4rem"
    )
