from libs.hello_world import HelloWorld


def test_greet():
    h = HelloWorld()
    assert h.my_attribute == 'whatever'


def test_capitalize():
    h = HelloWorld()
    test_string = "hello"
    result_string = "Hello"
    assert h.capitalize(test_string) == result_string


# this is not executed because does not start with `test_`
def func_test_capitalize():
    h = HelloWorld()
    test_string = "hello"
    result_string = "Hello"
    assert h.capitalize(test_string) == result_string
