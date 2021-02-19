from todo_item import TodoItem
from view_model import ViewModel

def test_to_do():
    items = [
        TodoItem(1, "Started Todo", "Not Started"),
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
    ]

    frank = ViewModel(items)

    # [TodoItem(1, "Started Todo", "Not Started")]
    todo_items = frank.to_do

    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Not Started"
