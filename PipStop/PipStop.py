# PipStop/PipStop.py

import reflex as rx
from PipStop.pages.home import home

app = rx.App()
app.add_page(home, route="/", title="Centre of Excellence")
app._compile()
