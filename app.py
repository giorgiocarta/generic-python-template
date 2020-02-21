from dotenv import find_dotenv, load_dotenv
from libs.hello_world import HelloWorld
import sys

load_dotenv(find_dotenv())


class App:

    def __init__(self, greetings: HelloWorld):
        self.greetings = greetings

    def run(self):
        print(self.greetings.greet())


def main():
    hello_world = HelloWorld()
    App(greetings=hello_world).run()
    print(sys.argv)


if __name__ == '__main__':
    main()
