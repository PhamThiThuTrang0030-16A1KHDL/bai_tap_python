import numpy as np
import pandas as pd
ser = pd.Series(np.random.random(20))
print(ser)
deciles = pd.qcut(ser, q=10, labels=False)
print(deciles)


