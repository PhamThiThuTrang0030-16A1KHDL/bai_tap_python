import pandas as pd
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
diff = ser - ser.shift(1)
print(diff)