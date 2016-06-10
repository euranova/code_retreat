import pytest
from my_module import my_function

def test_my_function():
    assert my_function(1, 3) == 4

def test_my_function_raises_exception():
    with pytest.raises(TypeError):
        my_function(1, '3')
