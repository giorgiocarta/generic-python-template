from os import getenv


class HelloWorld:

    def greet(self) -> str:
        return "{}".format(getenv('TEST_STRING', "Env file not loaded"))
