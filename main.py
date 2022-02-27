# %% [markdown]
# # Proyecto 2
#%%
import pandas as pd
# %%
df = pd.read_csv('synergy_logistics_database.csv')
# %%
#df.groupby('transport_mode').describe()['total_value']
# %%
imports = df[df['direction'] == 'Imports']
# %%
exports = df[df['direction'] == 'Exports']
# %%
rutas_export = exports.groupby(['origin', 'destination','transport_mode'])
# %%
rutas_export.count()['total_value'].sort_values(ascending=False).head(10)
# %%
rutas_import = imports.groupby(['origin', 'destination','transport_mode'])
# %%
# %%
rutas_import.count()['total_value'].sort_values(ascending=False).head(10)