import reflex as rx
from PipStop.components.navbar import navbar
from PipStop.components.call_to_action import call_to_action
from PipStop.components.footer import footer
from PipStop.components.new_post_form import new_post_form
from PipStop.components.post_card import post_card
from PipStop.state.community_state import CommunityState

@rx.page(route="/community")
def community() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.center(
                rx.container(
                    rx.vstack(
                        rx.heading("PipStop Community", size="4", color="white"),
                        rx.button(
                            "➕ New Post",
                            on_click=CommunityState.toggle_form,
                            color_scheme="blue",
                            size="2",
                        ),
                        rx.cond(CommunityState.show_form, new_post_form()),
                        rx.vstack(
                            rx.foreach(
                                CommunityState.posts,
                                lambda p: post_card(
                                    title=p["title"],
                                    body=p["body"],
                                    image=p.get("image"),
                                    author=p.get("author", "Tio")
                                )
                            ),
                            spacing="6",
                            width="100%",
                            align_items="center"
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    padding="4",
                )
            ),
    
            footer(),
            spacing="4",
            align="stretch",
        ),
        background_image="url('/image.png')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        padding="0",
    )
