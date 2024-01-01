import pandas as pd
import numpy as np
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(fruit.tolist())
print(weights.tolist())

df = pd.DataFrame({'fruit':fruit, 'weights':weights})
print("khối lượng trung bình của từng loại quả:\n",df.groupby('fruit').mean())
# print("khối lượng trung bình từng loại quả:\n", df)

