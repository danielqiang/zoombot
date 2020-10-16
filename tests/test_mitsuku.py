import pytest
from zoombot.mitsuku import Mitsuku


@pytest.fixture
def mitsuku() -> Mitsuku:
    with Mitsuku() as mitsuku:
        return mitsuku


@pytest.mark.parametrize(
    "message",
    [
        "Hello",
        "What is the weather like today in Seattle?"
        "Who are you?",
        "Tell me more about water please"
    ]
)
def test_mitsuku_basic(mitsuku, message):
    """Basic test to make sure mitsuku API responds
    with data without throwing an exception.
    """
    resp = mitsuku.send(message)
    assert len(resp) > 0
