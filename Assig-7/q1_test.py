import pandas as pd

# Cell 1
data = {'a': 10, 'b': 20, 'c': 30}
series = pd.Series(data)
print("Cell 1 output:\n", series)

# Cell 2
list_data = [5, 10, 15, 20]
series2 = pd.Series(list_data)
print("\nCell 2 output:\n", series2)

# Cell 3
data3 = [100, 200, 300, 400]
series3 = pd.Series(data3)
print("\nCell 3 outputs:")
print(series3[0])
print(series3[1:3])
