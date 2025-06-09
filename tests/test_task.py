import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.base import Task
from task_manager.advanced import AdvancedTask



def test_task_creation():
    t = Task("Write report", "high", "pending")
    assert t.priority == "high"
    assert t.status == "pending"
    assert str(t) == "[PENDING] HIGH: Write report"

def test_task_addition():
    t1 = Task("Task A")
    t2 = Task("Task B")
    combined = t1 + t2
    assert isinstance(combined, Task)
    assert "Task A + Task B" in str(combined)

def test_advanced_task_override():
    adv = AdvancedTask("Pay bills", "medium", "done", due_date="2025-06-15", recurring=True)
    display_output = adv.display()
    assert "Due: 2025-06-15" in display_output
    assert "Recurring" in display_output
