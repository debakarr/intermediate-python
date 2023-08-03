class _PrivateClass:
    ...


class NormalClass:
    def __init__(self) -> None:
        self.p = _PrivateClass()
        self._private_val = 5
        breakpoint()

    def public_meth(self):
        ...

    def _private_meth(self):
        ...

    def __mangaled_meth(self):
        ...


def public_func():
    ...


def _private_func():
    ...


NormalClass()
