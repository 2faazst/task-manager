import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.base import Task

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

def add_task(desc, priority, status, file_path="tasks.txt"):
    with open(file_path, "a") as f:
        f.write(f"{desc}|{priority}|{status}\n")

def test_add_task(tmp_path):
    file = tmp_path / "tasks.txt"
    add_task("Test task", "high", "pending", file_path=file)
    content = file.read_text().strip()
    assert content == "Test task|high|pending"

def test_view_tasks_output(tmp_path):
    file = tmp_path / "tasks.txt"
    file.write_text("Do laundry|medium|pending\n")

    from task_manager.base import task_generator
    tasks = list(task_generator(file))
    assert tasks[0]._description == "Do laundry"
    assert tasks[0].priority == "medium"
    assert tasks[0].status == "pending"

