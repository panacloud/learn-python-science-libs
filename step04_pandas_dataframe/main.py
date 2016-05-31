import numpy as np
import pandas as pd

f = pd.DataFrame(np.array([[1, 2], [3, 4], [5, 6]]), columns=["x", "y"],  index=["a", "b", "c"])
print(f)
