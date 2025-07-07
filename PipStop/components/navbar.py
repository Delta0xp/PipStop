import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/logo.png",width="1.7em",height="1.7em"),
        rx.text("PipStop", font_size="2xl", font_weight="bold", color="white"),
        rx.spacer(),
        rx.link("Home", href="/", color="white"),
        rx.text(" | "),
        rx.link("Community", href="/", color="white"),
        rx.text(" | "),
        rx.link("Discusion", href="/", color="white"),
        rx.text(" | "),
        rx.link("Mentor", href="/", color="white"),
        spacing="4",
        padding="1rem",
        background_color="#222222"
    )
