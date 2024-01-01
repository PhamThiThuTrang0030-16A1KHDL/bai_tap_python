import pandas as pd
import numpy as np
ser = pd.Series(np.random.randint(1, 10, 7))
print(ser)
print("Các vị trí có số là bội số của 3:\n",ser[ser % 3 == 0])