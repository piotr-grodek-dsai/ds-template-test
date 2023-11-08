import default.hello


def test_basic_test() -> None:
    default.hello.hello_world()
    assert True
