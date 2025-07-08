import reflex as rx

def membership_sign() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.text(
                    "Login or Sign Up",
                    font_size="2xl",
                    font_weight="bold",
                    margin_bottom="1rem",
                    color="white"
                ),
                rx.vstack(
                    rx.text("Email", align_self="flex-start", color="white"),
                    rx.input(placeholder="Enter your email", type="text", width="300px"),
                    spacing="1" 
                ),
                rx.vstack(
                    rx.text("Password", align_self="flex-start", color="white"),
                    rx.input(placeholder="Enter your password", type="password", width="300px"),
                    spacing="1" 
                ),
                rx.button("Confirm", color_scheme="pink", border_radius="0", width="100%", margin_top="1rem"),
                spacing="2",
                align="center"
            ),
            padding="2rem",
            background_color="#222222",
            border_radius="md",
            box_shadow="0 0 10px rgba(0,0,0,0.3)"
        ),
        padding_top="5rem"
    )

def page() -> rx.Component:
    return membership_sign()
