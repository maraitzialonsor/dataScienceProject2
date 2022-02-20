#%%
import pandas as pd
# %%
df = pd.read_csv('synergy_logistics_database.csv')
# %%
df.groupby('transport_mode').describe()['total_value']
# %%
