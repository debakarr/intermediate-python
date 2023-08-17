val8 = "global scope"

breakpoint()


def outer_func():
    val8 = "enclosing scope"
    breakpoint()

    def inner_func():
        val8 = "inner scope"
        breakpoint()

        print(f"Inside inner_func: {val8 = }")

    inner_func()


outer_func()
