import reflex as rx
from PipStop.components.navbar import navbar
from PipStop.components.hero import hero
from PipStop.components.call_to_action import call_to_action
from PipStop.components.footer import footer
from PipStop.components.post_card import post_card
from PipStop.components.new_post_form import new_post_form
from PipStop.state.community_state import CommunityState

@rx.page(route="/community")
def community() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            hero(),

            # Community section with post button, form, and posts
            rx.container(
                rx.vstack(
                    rx.heading("PipStop Community", size="4"),
                    rx.button(
                        "➕ New Post",
                        on_click=CommunityState.toggle_form,
                        color_scheme="blue",
                        margin_y="1em"
                    ),
                    rx.cond(
                        CommunityState.show_form,
                        new_post_form()
                    ),
                    rx.vstack(
                        rx.foreach(
                            CommunityState.posts,
                            lambda post: post_card(
                                title=post.title,
                                body=post.body,
                                author=post.author
                            )
                        )
                    ),
                    spacing="6",
                    width="100%",
                    padding="2em",
                    border_radius="xl",
                    box_shadow="lg",
                    background_color="whiteAlpha.900"
                ),
                padding_y="4em"
            ),

            call_to_action(),
            footer(),
            spacing="4",
            align="stretch"
        ),
        background_image="url('/image.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        min_height="100vh",
        padding="0"
    )
