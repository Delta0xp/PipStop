import reflex as rx

def post_card(title: str, body: str, image: rx.Var | None, author: str = "Tio"):
    return rx.card(
        rx.vstack(
            rx.text(title, size="4", weight="bold"),
            rx.text(f"by {author}", size="2", color="gray"),
            rx.text(body, size="2", margin_top="1"),
            rx.cond(
                image != None,
                rx.image(src=rx.get_upload_url(image), width="200px", margin_top="2"),
                None
            )
        ),
        padding="4",
        shadow="md",
        border_radius="lg",
        margin_y="4"
    )
