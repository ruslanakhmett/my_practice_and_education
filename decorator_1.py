'''For to catch exceptions'''

def suppress(exceptions, or_return=None):
    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except exceptions:
                return or_return
            return function(*args, **kwargs)
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
    return 1 // 0


print(foo())  # 42


@suppress((KeyError, IndexError))
def get_item(key, structure):
    return structure[key]


print(get_item(7, "foo")) is None  # True
print(get_item('a', {})) is None  # True
