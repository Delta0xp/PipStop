import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("Centre of Excellence", font_size="2xl", font_weight="bold", color="white"),
        rx.spacer(),
        rx.link("Home", href="/", style={"color": "#00FFFF", "text_decoration": "none"}),
        rx.link("Community", href="/community", style={"color": "#00FF99", "text_decoration": "none"}),
        rx.link("Mentors", href="/mentors", style={"color": "#FF00FF", "text_decoration": "none"}),
        rx.link("Login", href="/login", style={"color": "#FF8800", "text_decoration": "none"}),
        spacing="6",
        padding_x="2rem",
        padding_y="1rem",
        background_color="#111111",
        border_bottom="1px solid #333",
        width="100%",
        align="center"
    )
