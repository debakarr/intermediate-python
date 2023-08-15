_private_variable = 1

public_variable = 2


class _PrivateClass:
    ...


class PublicClass:
    ...


def _private_func():
    ...


def public_func():
    ...


class Example:
    def __mangled_method(self):
        ...

    def _private_method(self):
        ...

    def public_method(self):
        ...
