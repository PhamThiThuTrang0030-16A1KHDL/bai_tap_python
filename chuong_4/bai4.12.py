import pandas as pd
ser1 = pd.Series(range(5))
ser2 = pd.Series(list("abcde"))
print('Xếp chồng theo chiều dọc:\n',pd.concat([ser1,ser2]))
print('Xếp chồng theo chiều ngang:\n',pd.concat([ser1,ser2], axis=1))