from os import getenv


class HelloWorld:

    def __init__(self):
        self.my_attribute = "whatever"

    def greet(self) -> str:
        return "{}".format(getenv('TEST_STRING', "Env file not loaded"))

    def capitalize(self, word: str) -> str:
        return word.capitalize()
