import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "age": np.random.randint(22, 60, 100),
    "salary": np.random.randint(30000, 120000, 100)
})
df.to_csv("synthetic_salary.csv", index=False)
print(df.head())
