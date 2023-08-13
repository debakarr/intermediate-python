import numpy as np

def test_me():
    for i in range(6):
        x = np.array(range(10**7))
        y = np.array(np.random.uniform(0, 100, size=(10**8)))

test_me()
