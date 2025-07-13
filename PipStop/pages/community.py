# PipStop/PipStop/pages/community.py

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

            rx.center(  # Center the whole content horizontally
                rx.container(
                    rx.vstack(
                        rx.heading("PipStop Community", size="4"),
                        rx.button(
                            "➕ New Post",
                            on_click=CommunityState.toggle_form,
                            color_scheme="blue",
                            size="2"
                        ),
                        rx.cond(CommunityState.show_form, new_post_form()),

                        # Center the post cards
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
                            spacing="2",
                            align="center"  # This makes the cards centered inside the stack
                        ),

                        spacing="6",
                        width="100%",
                        align="center",
                    ),
                    size="2",  # small readable width for the container
                    padding="4"
                )
            ),

            call_to_action(),
            footer(),
            spacing="4",
            align="stretch"
        ),
        background_image="url('/image.png')",
        background_size="cover",
        min_height="100vh",
        padding="0"
    )
