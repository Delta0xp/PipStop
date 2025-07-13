import reflex as rx
from PipStop.state.community_state import CommunityState

def new_post_form():
    return rx.vstack(
        rx.upload("Select Image (optional)", id="file_upload"),
        rx.button(
            "Upload Image",
            on_click=CommunityState.handle_upload(rx.upload_files(upload_id="file_upload")),
            color_scheme="blue",
            size="2",
        ),
        rx.form(
            rx.vstack(
                rx.input(placeholder="Post Title", id="title"),
                rx.text_area(placeholder="What’s on your mind?", id="body"),
                rx.button("Submit Post", type_="submit", color="green", size="2"),
            ),
            on_submit=CommunityState.add_post,
            reset_on_submit=True,
            spacing="3",
        ),
        spacing="4",
    )
