import reflex as rx
from PipStop.pages.community import community    # ✅ Make sure this is imported
from PipStop.pages.home import home
from PipStop.pages.mentor import mentor
from PipStop.pages.discussion import discussion
from PipStop.pages.membership import page as membership

app = rx.App()

app.add_page(home, route="/", title="PipStop")
app.add_page(mentor, route="/mentor", title="Mentor")
app.add_page(discussion, route="/discussion", title="Discussion")
app.add_page(membership, route="/membership", title="Membership")
app.add_page(community, route="/community", title="Community")  # ✅ Even though decorated

# DO NOT call app.compile()
