import pandas as pd
import numpy as np
import matplotlib as plt
import os
from datetime import datetime

print('Directory Path: ',os.getcwd())
#print('Data Source Location: ',os.listdir())
#print("Path: aschmig/visual_analytics_final_project/20240227-scimaps-export.csv")
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = '20240227-scimaps-export.csv'
abs_file_path = os.path.join(script_dir, rel_path)
df = pd.read_csv(abs_file_path)
#print(df)

df = df.drop(['event_category', 'event_label'], axis=1)
df = df.dropna()
df['event_date'] = df['event_date'].astype('str')
df['event_date'] = df['event_date'].apply(lambda x: datetime.strptime(x,'%Y%m%d').strftime('%Y-%m-%d') )

def unix_converter(df_column):
    timestamp = df_column#.dropna()
    timestamp = timestamp.apply(lambda x: datetime.utcfromtimestamp((x/1000000)).strftime('%Y-%m-%d %H:%M:%S'))
    return timestamp


df['user_first_touch_cnvrtd'] = unix_converter(df['user_first_touch_timestamp'])
df['event_cnvrtd'] = unix_converter(df['event_timestamp'])
page_count = df['page_location'].value_counts().nlargest(5)
print('PAGES WITH HIGHEST INTERACTIONS:\n',page_count)


#This would calculate the duration spent by a single user, but some users' first timestamps go all the way back as early as 2023-06-21.
# There's no way someone spent over 8 months interacting on the same 
df['event_duration'] = df['event_timestamp'] - df['user_first_touch_timestamp']
max_duration = df.copy()
max_duration = max_duration.sort_values('event_duration',ascending=False).drop_duplicates(['user_pseudo_id'])


