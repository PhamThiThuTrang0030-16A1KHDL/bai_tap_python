import pandas as pd
import numpy as np
ser = pd.Series(list("abcddefghijkmnoprstuvwxyz"))
pos = [0, 4, 8, 14, 20]
print(ser.iloc[pos])