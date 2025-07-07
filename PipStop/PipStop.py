import reflex as rx
from PipStop.pages.home import home
from PipStop.pages.mentor import mentor
from PipStop.pages.community import community
from PipStop.pages.discussion import discussion
app = rx.App()
app.add_page(home, route="/", title="PipStop")
app.add_page(mentor, route="/mentor", title="Mentor")
app.add_page(community, route="/community", title="Community")
app.add_page(discussion, route="/discussion", title="Discussion")