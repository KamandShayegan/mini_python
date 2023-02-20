from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container, Horizontal
from learner import *

class Learner(Static):
    def compose(self) -> ComposeResult:
        yield Container(
            Horizontal(
                Button("Start", id="start", variant="success"),
                CardDisplay()
            )
        )
       

class CardDisplay(Static):
    """Display card"""

class LearnerApp(App):

    """A learning application to help you learn anything with flashcards."""

    # CSS_PATH = "learner.css"

    BINDINGS = [("q", "quit", "Quit The app"), ("d", "toggle_dark", "Toggle Dark Mode")]

    def compose(self) -> ComposeResult:
        """Creating child widgets."""
        yield Header()
        yield Footer()
        yield Learner()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = LearnerApp()
    app.run()

