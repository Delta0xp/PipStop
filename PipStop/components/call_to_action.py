import reflex as rx

def call_to_action() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "Ready to Level Up Your Tech Journey?",
                font_size="lg",
                font_weight="bold",
                color="white",
                text_align="center"
            ),
            rx.button(
                "Get Started Now",
                color_scheme="green",
                size="4",
                margin_top="1rem",
                margin_left="3rem",
                border_radius="0"
            ),
            spacing="3"

        ),
        background_color="#222222",
        padding_top="3rem",
        padding_bottom="3rem",
        
    )
