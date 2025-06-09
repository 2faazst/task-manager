from .base import Task
from .utils import deco

class AdvancedTask(Task):
    def __init__(self, description: str, priority: str = "low", status: str = "pending",
                 due_date: str = None, recurring: bool = False):
        super().__init__(description, priority, status)
        self.due_date = due_date
        self.recurring = recurring

    # Override display method with additional info
    @deco("magenta")
    def display(self):
        base = super().__str__()
        extras = []
        if self.due_date:
            extras.append(f"Due: {self.due_date}")
        if self.recurring:
            extras.append("🔁 Recurring")
        return f"{base} {' | '.join(extras)}"
