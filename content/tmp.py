import pytest


@pytest.fixture(autouse=True, scope="session")
def setup_and_teardown_example():
    print("Setup - Before the test")
    yield
    print("Teardown - After the test")


def test_add():
    print("Running test_add")
    assert 1 + 1 == 2


def test_sub():
    print("Running test_sub")
    assert 1 - 1 == 0
