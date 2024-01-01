import numpy as np
import pandas as pd
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
top2 = ser.value_counts().head(2)
print(top2)
ser = ser.where(ser.isin(top2.index), other="Other")
print(ser)

