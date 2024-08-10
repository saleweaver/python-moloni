import os
import re


def main():
    from moloni.base import __all__ as base

    api_files = os.listdir("../moloni/api")
    base_files = os.listdir("../moloni/base")

    exports = (
        [
            "moloni.api",
            "moloni.base",
        ]
        + [
            "moloni.api." + re.sub(".py", "", x)
            for x in api_files
            if x != "__init__.py" and x != "_cache__"
        ]
        + [
            "moloni.base." + re.sub(".py", "", x)
            for x in base
            if x != "__init__.py" and x != "_cache__"
        ]
    )

    print(exports)


if __name__ == "__main__":
    main()
