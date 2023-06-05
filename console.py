import functools
import sys
import inspect
import gc
from typing import Any


class console:
    def __init__(self, func):
        self.func = func
        self.clear()
        functools.wraps(self.func, func)

    def __call__(self, *args: Any, **kwargs: Any):
        self.func(*args, **kwargs)

    def clear(self):
        self.__console__ = []

    def write(self, *values: object, sep: str = " ", end: str = "\n"):
        string = sep.join(map(str, values)) + end
        lines = string.split("\n")

        frame = sys._getframe(3)
        info = inspect.getframeinfo(frame)

        sys.stdout.write(
            f'File "{info.filename}"\n'
            + f'scope: "{info.function}"\n'
            + f"line: {info.lineno}\n"
            + f'"{info.code_context[0].strip()}"'
            + "\n"
        )

        sys.stdout.write("> " + lines[0] + "\n")
        for line in lines[1:]:
            sys.stdout.write("  " + line + "\n")
        sys.stdout.write("\n")

        self.__console__ += {
            "string": string,
            "lineno": info.lineno,
            "filename": info.filename,
        }
        return string

    def reduced(self):
        self.write(*[log["string"] for log in self.__console__])
        return self.__console__


if __name__ == "__main__":

    def g():
        @console
        def f(n):
            for i in range(1, n + 1):
                f.write(*["*" * j for j in range(1, i + 1)])
            # return f.reduced()

        f(5)

    g()
