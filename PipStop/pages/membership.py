# PipStop/pages/membership.py

import reflex as rx
from PipStop.components.navbar import navbar

class ViewState(rx.State):
    is_signup: bool = True

    def toggle_view(self):
        self.is_signup = not self.is_signup

def membership_sign() -> rx.Component:
    return rx.box(
        navbar(),

        rx.center(
            rx.box(
                rx.vstack(
                    # Title
                    rx.text(
                        rx.cond(ViewState.is_signup, "Sign Up", "Login"),
                        font_size="2xl",
                        font_weight="bold",
                        margin_bottom="1rem",
                        color="white"
                    ),

                    # Email input
                    rx.vstack(
                        rx.text("Email", align_self="flex-start", color="white"),
                        rx.input(placeholder="Enter your email", type="text", width="300px"),
                        spacing="1"
                    ),

                    # Password input
                    rx.vstack(
                        rx.text("Password", align_self="flex-start", color="white"),
                        rx.input(placeholder="Enter your password", type="password", width="300px"),
                        spacing="1"
                    ),

                    # Only show Role dropdown on signup
                    rx.cond(
                        ViewState.is_signup,
                        rx.vstack(
                            rx.text("Role", align_self="flex-start", color="white"),
                            rx.select(["Member", "Mentor"], placeholder="Select role", width="300px"),
                            spacing="1"
                        ),
                        rx.box()  # empty if login
                    ),

                    # Submit button (no logic yet)
                    rx.button(
                        rx.cond(ViewState.is_signup, "Sign Up", "Login"),
                        color_scheme="pink",
                        border_radius="0",
                        width="100%",
                        margin_top="1rem",
                        cursor="pointer",
                    ),

                    # Toggle button
                    rx.button(
                        rx.cond(ViewState.is_signup, "Switch to Login", "Switch to Sign Up"),
                        on_click=ViewState.toggle_view,
                        variant="ghost",
                        width="100%",
                        margin_top="0.5rem",
                        cursor="pointer",
                        style={
                            "outline": "none",
                            "boxShadow": "none",
                            "background": "transparent",
                        },
                        _hover={"background": "transparent"},
                        _focus={"background": "transparent"},
                    ),

                    spacing="2",
                    align="center"
                ),
                padding="2rem",
                background_image="url('/image.png')",
                background_size="cover",
                background_position="center",
                background_repeat="no-repeat",
                border_radius="md",
                box_shadow="0 0 10px rgba(0,0,0,0.3)"
            ),
            padding="30vh",
        ),

        background_image="url('/image.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        min_height="100vh",
        padding="0"
    )

def page() -> rx.Component:
    return membership_sign()
