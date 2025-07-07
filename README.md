# PipStop

# Nav Bar

Certainly! Here's a concise and shareable guide to implementing navigation in a Reflex application. This blueprint outlines the steps to add new pages and integrate them into the navigation bar, ensuring a consistent structure across your project.

---

## 🧭 Reflex Navigation Workflow

### 1. **Create a New Component (Optional)**

If your new page requires a unique component:

* **File Location:** `PipStop/components/your_component.py`

* **Function Definition:** Define a function that returns a Reflex component. The function name should match the file name for consistency.

  ```python
  # PipStop/components/your_component.py
  import reflex as rx

  def your_component() -> rx.Component:
      return rx.box(
          rx.text("Your Component Content"),
          padding="2rem",
          background_color="#111111",
          min_height="100vh"
      )
  ```

### 2. **Create the Page**

* **File Location:** `PipStop/pages/your_page.py`

* **Function Definition:** Define a function that returns a Reflex component, incorporating the component created in step 1.

  ```python
  # PipStop/pages/your_page.py
  import reflex as rx
  from PipStop.components.navbar import navbar
  from PipStop.components.your_component import your_component
  from PipStop.components.footer import footer

  def your_page() -> rx.Component:
      return rx.box(
          rx.vstack(
              navbar(),
              your_component(),
              footer(),
              spacing="4",
              align="stretch"
          ),
          background_color="#111111",
          min_height="100vh",
          padding="0"
      )
  ```

### 3. **Update the Navbar**

* **File Location:** `PipStop/components/navbar.py`

* **Add Link:** Include a new link that points to the route of your new page.

  ```python
  # PipStop/components/navbar.py
  import reflex as rx

  def navbar() -> rx.Component:
      return rx.hstack(
          rx.link("Home", href="/", color="white"),
          rx.link("Your Page", href="/your-page", color="white"),
          spacing="4",
          padding="1rem",
          background_color="#1a1a1a"
      )
  ```

### 4. **Register the Page in the Application**

* **File Location:** `PipStop/PipStop.py`

* **Import and Add Page:** Import your page function and register it with a route and title.

  ```python
  # PipStop/PipStop.py
  import reflex as rx
  from PipStop.pages.home import home
  from PipStop.pages.your_page import your_page

  app = rx.App()
  app.add_page(home, route="/", title="PipStop")
  app.add_page(your_page, route="/your-page", title="Your Page")
  ```

### 5. **Run the Application**

* **Command:** In your project's root directory, execute:

  ```bash
  reflex run
  ```

* **Access:** Navigate to `http://localhost:3000` in your browser. You should see the updated navbar with a link to "Your Page." Clicking it will take you to the new page.

---

By following this blueprint, you and your colleagues can systematically add new pages and corresponding navigation links to your Reflex application. This approach promotes consistency and maintainability across your project.

If you need further assistance or have questions about more advanced features, feel free to ask!


# Backend

''' bash

(site) PS C:\Users\mithe\Documents\Github\PipStop> uvicorn Backend.main:app --reload
 --port 8000

'''


# Frpmtend

''' bash

(site) PS C:\Users\mithe\Documents\Github\PipStop> reflex run

'''


# Installation notes:

## Make sure to install requests