import pandas as pd
import numpy as np
import matplotlib as plt
import os

print('Directory Path: ',os.getcwd())

print('Data Source Location: ',os.path.dirname('20240227-scimaps-export.csv'))

df = pd.read_csv('20240227-scimaps-export.csv')
print(df)