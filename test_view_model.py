from todo_item import TodoItem
from view_model import ViewModel

def test_to_do():
    # Arrange
    items = [
        TodoItem(1, "Started Todo", "Not Started"),
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
    ]

    frank = ViewModel(items)

    # Act
    # [TodoItem(1, "Started Todo", "Not Started")]
    todo_items = frank.to_do

    # Assert
    assert len(todo_items) == 1

    todo_item = todo_items[0]

    assert todo_item.status == "Not Started"

def test_doing():
    # Arrange
    items = [
        TodoItem(1, "Started Todo", "Not Started"),
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
    ]

    vader = ViewModel(items)

    # Act
    doing_items = vader.doing
    
    # Assert
    assert len(doing_items) == 1

    doing_item = doing_items[0]

    assert doing_item.status == "In Progress"
    assert doing_item.id == 2

def test_done():

    items = (
        TodoItem(1, "Started Todo", "Not Started"), 
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
    )
    storm = ViewModel(items)

    done_items = storm.done
    
    assert len(done_items) == 1

    done_item = done_items[0]

    assert done_item.status == "Completed"
    assert done_item.id == 3

def test_show_all_done_items_returns_true_for_small_numbers_of_items():
    # Arrange
    items = [
        TodoItem(1, "Started Todo", "Not Started"),
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
    ]

    vader = ViewModel(items)

    # Act
    result = vader.show_all_done_items
    
    # Assert
    assert result == True

def test_show_all_done_items_returns_false_for_large_numbers_of_items():
    # Arrange
    items = [
        TodoItem(1, "Started Todo", "Not Started"),
        TodoItem(2, "Doing Todo", "In Progress"),
        TodoItem(3, "Done Todo", "Completed"),
        TodoItem(4, "Done Todo", "Completed"),
        TodoItem(5, "Done Todo", "Completed"),
        TodoItem(6, "Done Todo", "Completed"),
        TodoItem(7, "Done Todo", "Completed"),
        TodoItem(8, "Done Todo", "Completed"),
    ]

    vader = ViewModel(items)

    # Act
    result = vader.show_all_done_items
    
    # Assert
    assert result == False