from src import example

def test_add():
    assert example.add(2, 3) == 5
    assert example.add('space', 'ship') == 'spaceship'

def test_subtract():
    assert example.subtract(2, 3) == -1

