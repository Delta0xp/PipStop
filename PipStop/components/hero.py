import reflex as rx

class HeroState(rx.State):
    def go_to_membership(self):
        rx.toast("Redirecting to membership page...", duration=2000)
        return rx.redirect("/membership") 

def hero() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text(
                "Empowering the Next Generation in Cloud, AI, Data & Automation",
                font_size="4xl",
                font_weight="bold",
                color="white",
                text_align="center",
                text_shadow="0 0 4px #FFFFFF, 0 0 8px #FFFFFF"
            ),
            rx.text(
                "Mentorship, Community, and Discussions — all in one place.",
                font_size="md",
                color="#FFFFFF",
                text_align="center",
                text_shadow="0 0 8px #FFFFFF, 0 0 16px #FFFFFF"
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
                    border_radius="0",
                    on_click=HeroState.go_to_membership
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
