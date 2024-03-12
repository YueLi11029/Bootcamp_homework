#question_3
'''
3) How to get the rows of a dataframe with row sum > 100?
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

rows_greater_100 = df[df.sum(axis=1) > 100]


print(rows_greater_100)
