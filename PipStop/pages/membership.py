import reflex as rx
import requests

class MembershipState(rx.State):
    email: str
    password: str
    role: str = "member"

    message: str = ""
    is_signup: bool = True
    token: str = ""

    def toggle_mode(self):
        self.is_signup = not self.is_signup
        self.message = ""

    def submit(self):
        try:
            payload = {
                "email": self.email,
                "password": self.password,
            }

            if self.is_signup:
                payload["role"] = self.role
                response = requests.post("http://127.0.0.1:8000/api/auth/signup", json=payload)
                if response.status_code == 200:
                    self.message = "Signup successful! You can now log in."
                else:
                    self.message = f"Error: {response.json().get('detail', 'Signup failed.')}"
            else:
                response = requests.post("http://127.0.0.1:8000/api/auth/login", json=payload)
                if response.status_code == 200:
                    data = response.json()
                    self.token = data["access_token"]
                    self.message = "Login successful!"
                else:
                    self.message = f"Error: {response.json().get('detail', 'Login failed.')}"
        except Exception as e:
            self.message = f"Exception: {e}"

def membership_sign() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                rx.text(
                    rx.cond(MembershipState.is_signup, "Sign Up", "Login"),
                    font_size="2xl",
                    font_weight="bold",
                    margin_bottom="1rem",
                    color="white"
                ),
                rx.vstack(
                    rx.text("Email", align_self="flex-start", color="white"),
                    rx.input(placeholder="Enter your email", type="text", on_change=MembershipState.set_email, width="300px"),
                    spacing="1" 
                ),
                rx.vstack(
                    rx.text("Password", align_self="flex-start", color="white"),
                    rx.input(placeholder="Enter your password", type="password", on_change=MembershipState.set_password, width="300px"),
                    spacing="1" 
                ),
                rx.cond(
                    MembershipState.is_signup,
                    rx.vstack(
                        rx.text("Role", align_self="flex-start", color="white"),
                        rx.select(["member", "mentor"], on_change=MembershipState.set_role, placeholder="Select role", width="300px"),
                        spacing="1"
                    ),
                    rx.box()  # Empty when login
                ),
                rx.button(
                    rx.cond(MembershipState.is_signup, "Sign Up", "Login"),
                    on_click=MembershipState.submit,
                    color_scheme="pink",
                    border_radius="0",
                    width="100%",
                    margin_top="1rem"
                ),
                rx.button(
                    rx.cond(MembershipState.is_signup, "Switch to Login", "Switch to Sign Up"),
                    on_click=MembershipState.toggle_mode,
                    variant="ghost",
                    width="100%",
                    margin_top="0.5rem"
                ),
                rx.text(MembershipState.message, color="white"),
                spacing="2",
                align="center"
            ),
            padding="2rem",
            background_image="url('/image.png')",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            border_radius="md",
            box_shadow="0 0 10px rgba(0,0,0,0.3)"
        ),
        background_image="url('/image.png')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        min_height="100vh",
        padding="0"
    )

def page() -> rx.Component:
    return membership_sign()
