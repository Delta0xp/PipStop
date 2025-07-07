import reflex as rx

import requests

def get_backend_message():
    try:
        response = requests.get("http://127.0.0.1:8000/api/TEST")
        if response.status_code == 200:
            return response.json().get("message", "No message found")
        else:
            return "Error fetching message"
    except Exception as e:
        return f"Exception: {e}"


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/logo.png",width="1.7em",height="1.7em"),
        rx.text("PipStop", font_size="2xl", font_weight="bold", color="white"),
        rx.spacer(),
        rx.link("Home", href="/", color="white"),
        rx.text(" | "),
        rx.link("Community", href="/community", color="white"),
        rx.text(" | "),
        rx.link("Discusion", href="/discussion", color="white"),
        rx.text(" | "),
        rx.link("Mentor", href="/mentor", color="white"),
        spacing="4",
        padding="2rem",
        # background_color="#222222"
    )
