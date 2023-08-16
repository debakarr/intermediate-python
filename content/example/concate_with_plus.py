@profile
def add_string_with_plus(iters):
    s = ""
    for i in range(iters):
        s += "abc"
    assert len(s) == 3*iters
    
add_string_with_plus(50000)
