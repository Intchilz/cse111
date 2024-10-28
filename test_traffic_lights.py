import pytest
from unittest.mock import MagicMock
import time
from traffic_light import green,greenb,orange,orangeb,red,redb

# Mocking the necessary objects and functions
class MockCanvas:
    def create_oval(self, x1, y1, x2, y2, fill, width):
        return (x1, y1, x2, y2, fill, width)

# Assuming that 'a' is defined globally for the functions
a = 1  # Set this to the desired value for testing

def test_green():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    green()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Green'

def test_greenb():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    greenb()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Black'

def test_orange():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    orange()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Orange'

def test_orangeb():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    orangeb()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Black'

def test_red():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    red()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Red'

def test_redb():
    global myCanvas, traffic_lights
    myCanvas = MockCanvas()
    traffic_lights = MagicMock()
    
    redb()
    
    assert myCanvas.create_oval.call_count == a
    args, kwargs = myCanvas.create_oval.call_args
    assert kwargs['fill'] == 'Black'

# Note: In a real-world scenario, it's better to control time-dependent functions with mocking as well,
# to avoid waiting during tests. The time.sleep calls can be removed or replaced in the actual code.
