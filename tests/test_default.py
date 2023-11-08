import default.hello


def test_basic_test() -> None:
    default.hello.hello_world()
    assert True

def test_something() -> None:
    assert 0 != 1