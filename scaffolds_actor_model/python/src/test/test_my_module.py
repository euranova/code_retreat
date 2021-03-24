import pytest
import thespian.actors as ta
from my_module import MyClass, get_actor_by_name

def test_my_class_init():
    instance = MyClass()
    assert instance.given_address is None

def test_actor_creation_raises_exception():
    with pytest.raises(TypeError):
        ta.ActorSystem().createActor()
