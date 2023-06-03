import functools
import sys


class console:
    console = ""

    @classmethod
    def clear(cls):
        cls.console = ""

    @classmethod
    def write(cls, *values: object, sep: str = " ", end: str = "\n"):
        string = sep.join(map(str, values)) + end

        sys.stdout.write(string)
        cls.console += string
        return string

    @classmethod
    def reduced(cls):
        sys.stdout.write(cls.console)
        return cls.console

    @staticmethod
    def use_console(func):
        console.clear()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper


if __name__ == "__main__":

    @console.use_console
    def f(n):
        for i in range(n):
            console.write(i)
        return console.reduced()

    f(5)
