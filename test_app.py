import pytest
import trello_items as app
 

def add(x,y):
    return x + y


def test_add():
    assert add(2,3) == 5
    assert add(1,-1) == 0

def test_view_model(todo):
    todo = [{"id": 1, "Status": In Progress, "title": "wash dog"}]
    results = [{"id": 1, "Status": In Progress, "title": "wash dog"}]
    view_model = app.ViewModel(todo)
    assert view_model.trello_items == results


