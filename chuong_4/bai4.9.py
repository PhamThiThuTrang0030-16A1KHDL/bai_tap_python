import pandas as pd
import numpy as np
ser = pd.Series(np.random.randint(1, 10, 35))
ser = pd.DataFrame(np.random.randint(1, 10, size=(7,5)))
print(ser)