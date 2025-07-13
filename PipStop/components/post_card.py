import reflex as rx

def post_card(title: str, body: str, image: str = "", author: str = "Anonymous") -> rx.Component:
    return rx.box(
        rx.card(
            rx.vstack(
                rx.heading(title, size="5", color="white"),
                rx.text(f"by {author}", size="1", color="gray"),
                rx.text(body, color="white", size="3"),
                rx.cond(
                    image != "",
                    rx.image(
                        src=image,
                        width="100%",
                        height="auto",
                        border_radius="lg",
                        margin_top="4px"
                    )
                )
            ),
            padding="4",
            background_color="rgba(255,255,255,0.05)",
            border_radius="xl",
            shadow="lg",
            width="100%",
        ),
        width="100%",
        max_width="800px",
        margin_y="4",
        align_self="center"
    )
