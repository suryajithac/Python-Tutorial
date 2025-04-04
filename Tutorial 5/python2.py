import pandas as pd
names = ['anu', 'ram', 'tom']
data = pd.DataFrame(names, index=['id1', 'id2', 'id3'])
print("DataFrame with index:")
print(data)