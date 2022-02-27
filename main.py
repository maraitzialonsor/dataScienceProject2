# %% [markdown]
# # Proyecto 2
#%%
import pandas as pd
# %%
df = pd.read_csv('synergy_logistics_database.csv')
# %%
df.groupby('transport_mode').describe()['total_value']
# %%
imports = df[df['direction'] == 'Imports']
print(imports)
# %%
exports = df[df['direction'] == 'Exports']
print(imports)
# %%
rutas = exports.groupby(['origin', 'destination','transport_mode'])
# %%
rutas.count()['total_value'].sort_values(ascending=False)

# %%
