import pandas as pd
import numpy as np
import matplotlib as plt
import os

print('Directory Path: ',os.getcwd())
#print('Data Source Location: ',os.listdir())
#print("Path: aschmig/visual_analytics_final_project/20240227-scimaps-export.csv")
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '20240227-scimaps-export.csv'
abs_file_path = os.path.join(script_dir, rel_path)
df = pd.read_csv(abs_file_path)
print(df)