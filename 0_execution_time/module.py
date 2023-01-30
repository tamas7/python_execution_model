print("Module scope")


class Class:
    print("Class scope")

    @staticmethod
    def method():
        print("Method scope")


def decorator(func):
    print("Decorator scope")
    return func


@decorator
def function():
    print("Function scope")
