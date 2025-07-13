import reflex as rx
from typing import List

class CommunityState(rx.State):
    show_form: bool = False

    class Post(rx.Base):
        title: str
        body: str
        author: str

    posts: List[Post] = []

    def toggle_form(self):
        self.show_form = not self.show_form

    def add_post(self, form_data: dict):
        title = form_data.get("title", "").strip()
        body = form_data.get("body", "").strip()
        if title and body:
            self.posts.append(self.Post(title=title, body=body, author="Tio"))
        self.show_form = False
