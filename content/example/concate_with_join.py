@profile
def add_string_with_join(iters):
    l = []
    for i in range(iters):
        l.append("abc")
    s = "".join(l)
    assert len(s) == 3 * iters


add_string_with_join(50000)
