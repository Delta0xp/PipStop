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

def backend_message_component() -> rx.Component:
    message = get_backend_message()
    return rx.text(message, color="cyan", font_weight="bold", padding_top="1rem")
