# %% [markdown]
# # Proyecto 2
#%%
import pandas as pd
# %%
df = pd.read_csv('synergy_logistics_database.csv')
# %%
imports = df[df['direction'] == 'Imports']
exports = df[df['direction'] == 'Exports']
# %%
# Rutas de exportación
rutas_export = exports.groupby(['origin', 'destination','transport_mode'])
rutas_export.count()['total_value'].sort_values(ascending=False).head(10)
# %%
# Rutas de importación 
rutas_import = imports.groupby(['origin', 'destination','transport_mode'])
rutas_import.count()['total_value'].sort_values(ascending=False).head(10)

# %%
# Medio de transporte utilizado en importaciones
imports.groupby(by=['transport_mode']).sum().groupby(level=[0]).cumsum()['total_value'].sort_values(ascending=False)
# %%
# Medio de transporte utilizado en exportaciones
exports.groupby(by=['transport_mode']).sum().groupby(level=[0]).cumsum()['total_value'].sort_values(ascending=False)
# %%
# Obtenemos el total_value de importaciones y exportaciones
total_imports = int(imports['total_value'].sum())
total_exports = int(exports['total_value'].sum())
# %%
# Nuevo dataframe para obtener porcentajes de importaciones por país
# Frecuencia acumulada de importaciones 
imports_pais = pd.DataFrame(imports.groupby(by=['origin']).sum().groupby(level=[0]).cumsum()['total_value'].sort_values(ascending=False))
imports_pais['porcentaje'] = imports_pais['total_value']*100/total_imports
imports_pais['acum'] = (imports_pais['porcentaje']).cumsum()
print(imports_pais[:8])
# %%
# Frecuencia acumulada de exportaciones 
exports_pais = pd.DataFrame(exports.groupby(by=['origin']).sum().groupby(level=[0]).cumsum()['total_value'].sort_values(ascending=False))
exports_pais['porcentaje'] = exports_pais['total_value']*100/total_exports
exports_pais['acum'] = (exports_pais['porcentaje']).cumsum()
print(exports_pais[:8])

# %%
