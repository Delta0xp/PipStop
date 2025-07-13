import reflex as rx
from PipStop.state.community_state import CommunityState

def new_post_form():
    return rx.form(
        rx.vstack(
            rx.input(placeholder="Post Title", id="title"),
            rx.text_area(placeholder="What's on your mind?", id="body"),
            rx.button("Submit", type_="submit", color="green"),
        ),
        on_submit=CommunityState.add_post,
        reset_on_submit=True,
        width="100%",
        padding="1em",
        border="1px solid #ccc",
        border_radius="xl",
        box_shadow="md",
    )
