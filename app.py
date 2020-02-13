from dotenv import find_dotenv, load_dotenv
from os import getenv

load_dotenv(find_dotenv())


class App:

    def __init__(self):
        pass

    def run(self):
        print("{}".format(getenv('TEST_STRING', "Env file not loaded")))


def main():
    App().run()


if __name__ == '__main__':
    main()
