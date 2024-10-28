import pytest
from unittest.mock import MagicMock
from traffic_lights import red, redb, orange, orangeb, green, greenb

@pytest.fixture
def mock_canvas():
    return MagicMock()

def test_red(mock_canvas):
    a = 1  # Test with a single cycle
    red(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 250, 200, 350, fill='Red', width=2)

def test_redb(mock_canvas):
    a = 1  # Test with a single cycle
    redb(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 250, 200, 350, fill='Black', width=2)

def test_orange(mock_canvas):
    a = 1  # Test with a single cycle
    orange(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 150, 200, 250, fill='Orange', width=2)

def test_orangeb(mock_canvas):
    a = 1  # Test with a single cycle
    orangeb(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 150, 200, 250, fill='Black', width=2)

def test_green(mock_canvas):
    a = 1  # Test with a single cycle
    green(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 50, 200, 150, fill='Green', width=2)

def test_greenb(mock_canvas):
    a = 1  # Test with a single cycle
    greenb(mock_canvas, a)
    assert mock_canvas.create_oval.call_count == a
    mock_canvas.create_oval.assert_called_with(100, 50, 200, 150, fill='Black', width=2)

pytest.main(["-v", "--tb=line", "-rN", __file__])
