def main():
    from moloni.api import __all__ as api
    from moloni.base import __all__ as base

    exports = (
        [
            "moloni.api",
            "moloni.base",
        ]
        + ["moloni.api." + x for x in api]
        + ["moloni.base." + x for x in base]
    )

    print(exports)


if __name__ == "__main__":
    main()
