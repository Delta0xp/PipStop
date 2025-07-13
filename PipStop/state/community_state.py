import reflex as rx
from typing import List
import random
import string

def make_unique(filename: str) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=8)) + "_" + filename

class CommunityState(rx.State):
    show_form: bool = False
    posts: List[dict] = []
    uploaded_image: str | None = None

    def toggle_form(self):
        self.show_form = not self.show_form

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        for file in files:
            data = await file.read()
            name = make_unique(file.name)
            path = upload_dir / name
            with path.open("wb") as f:
                f.write(data)
            self.uploaded_image = name

    def add_post(self, form_data: dict):
        title = form_data.get("title", "").strip()
        body = form_data.get("body", "").strip()
        img = self.uploaded_image
        if title and body:
            self.posts.append({
                "title": title,
                "body": body,
                "image": img,
                "author": "Tio"
            })
        # reset
        self.uploaded_image = None
        self.show_form = False
