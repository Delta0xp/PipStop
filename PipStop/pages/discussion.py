import reflex as rx
from PipStop.components.navbar import navbar
from PipStop.components.hero import hero
from PipStop.components.feat import features
from PipStop.components.testimonial import testimonials
from PipStop.components.call_to_action import call_to_action
from PipStop.components.footer import footer
from PipStop.components.discussion_section import discussion_section

def discussion() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            hero(),
            discussion_section(),
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
