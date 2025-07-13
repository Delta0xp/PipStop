import reflex as rx

def post_card(title: str, body: str, author: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.text(title, size="4", weight="bold"),  # ✅ fixed size
                rx.spacer(),
                rx.text(f"by {author}", size="2", color="gray"),  # ✅ fixed size
            ),
            rx.text(body, size="2", margin_y="0.5em"),  # ✅ fixed size
        ),
        padding="1.5em",
        shadow="md",
        border_radius="xl",
        margin_y="1em"
    )
