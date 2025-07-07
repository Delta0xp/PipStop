import reflex as rx
from PipStop.components.navbar import navbar

def home() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            # Hero Section
            rx.center(
                rx.vstack(
                    rx.text(
                        "Empowering the Next Generation in Cloud, AI, Data & Automation",
                        font_size="2xl",
                        font_weight="bold",
                        color="white",
                        text_align="center"
                    ),
                    rx.text(
                        "Mentorship, Community, and Discussions — all in one place.",
                        font_size="md",
                        color="#AAAAAA",
                        text_align="center"
                    ),
                    rx.hstack(
                        rx.button("Join the Community", color_scheme="pink", size="3"),
                        rx.button("Become a Mentor", color_scheme="cyan", size="3"),
                        spacing="4",
                        padding_top="1rem"
                    ),
                    spacing="3"
                ),
                padding_top="4rem",
                padding_bottom="4rem"
            ),

            # Features Section
            rx.center(
                rx.vstack(
                    rx.text("Why Join Us?", font_size="xl", font_weight="bold", color="white"),
                    rx.hstack(
                        rx.box(
                            rx.text("💡", font_size="3xl"),
                            rx.text("Expert Mentorship", font_weight="semibold", color="white"),
                            rx.text("Learn directly from experienced professionals.", color="#AAAAAA"),
                            padding="1rem",
                            background_color="#222222",
                            border_radius="xl",
                            width="200px",
                            text_align="center"
                        ),
                        rx.box(
                            rx.text("🤝", font_size="3xl"),
                            rx.text("Vibrant Community", font_weight="semibold", color="white"),
                            rx.text("Connect and grow with like-minded peers.", color="#AAAAAA"),
                            padding="1rem",
                            background_color="#222222",
                            border_radius="xl",
                            width="200px",
                            text_align="center"
                        ),
                        rx.box(
                            rx.text("🚀", font_size="3xl"),
                            rx.text("Career Growth", font_weight="semibold", color="white"),
                            rx.text("Access opportunities and stay ahead.", color="#AAAAAA"),
                            padding="1rem",
                            background_color="#222222",
                            border_radius="xl",
                            width="200px",
                            text_align="center"
                        ),
                        spacing="5"
                    ),
                    spacing="4"
                ),
                padding_top="4rem",
                padding_bottom="4rem"
            ),

            # Testimonials Section
            rx.center(
                rx.vstack(
                    rx.text("What Our Members Say", font_size="xl", font_weight="bold", color="white"),
                    rx.hstack(
                        rx.box(
                            rx.text("“An inspiring community that pushes me to be my best!”", color="#AAAAAA", font_style="italic"),
                            rx.text("— Alex, Data Engineer", color="white", margin_top="0.5rem"),
                            padding="1rem",
                            background_color="#1a1a1a",
                            border_radius="xl",
                            width="250px"
                        ),
                        rx.box(
                            rx.text("“The mentorship here accelerated my career like nothing else.”", color="#AAAAAA", font_style="italic"),
                            rx.text("— Sam, AI Researcher", color="white", margin_top="0.5rem"),
                            padding="1rem",
                            background_color="#1a1a1a",
                            border_radius="xl",
                            width="250px"
                        ),
                        rx.box(
                            rx.text("“I finally found my tribe. Knowledge-sharing at its finest!”", color="#AAAAAA", font_style="italic"),
                            rx.text("— Jamie, Cloud Architect", color="white", margin_top="0.5rem"),
                            padding="1rem",
                            background_color="#1a1a1a",
                            border_radius="xl",
                            width="250px"
                        ),
                        spacing="5"
                    ),
                    spacing="4"
                ),
                padding_top="4rem",
                padding_bottom="4rem"
            ),

            # Call-to-Action Banner
            rx.center(
                rx.vstack(
                    rx.text("Ready to Level Up Your Tech Journey?", font_size="lg", font_weight="bold", color="white", text_align="center"),
                    rx.button("Get Started Now", color_scheme="green", size="4", margin_top="1rem"),
                    spacing="3"
                ),
                background_color="#222222",
                padding_top="3rem",
                padding_bottom="3rem"
            ),

            # Footer
            rx.center(
                rx.vstack(
                    rx.text("© 2025 Centre of Excellence • Built with Reflex", color="#888888", font_size="sm"),
                    rx.hstack(
                        rx.link("Twitter", href="https://twitter.com", color="#AAAAAA"),
                        rx.link("LinkedIn", href="https://linkedin.com", color="#AAAAAA"),
                        rx.link("GitHub", href="https://github.com", color="#AAAAAA"),
                        spacing="4"
                    ),
                    spacing="2"
                ),
                padding="2rem"
            ),

            spacing="4",
            align="stretch"
        ),
        background_color="#111111",
        min_height="100vh",
        padding="0"
    )
