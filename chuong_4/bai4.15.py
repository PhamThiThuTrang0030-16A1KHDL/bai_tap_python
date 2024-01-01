import pandas as pd
import numpy as np
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
ser = ser.str.capitalize()
print(ser)