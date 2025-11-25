import numpy as np
import pandas as pd

# ===============================================================
# 1. Generar datos sintéticos
# ===============================================================
# Simulamos 100 mediciones experimentales
np.random.seed(0)  # para que los resultados sean replicables

temperatura = np.random.normal(25, 2, 100)   # media 25, sigma 2
presion     = np.random.normal(1.01, 0.1, 100)
tiempo      = np.random.normal(60, 5, 100)

# Crear matriz y guardar CSV
data = np.column_stack((temperatura, presion, tiempo))
np.savetxt("datos_sinteticos.csv", data, delimiter=",", 
           header="temperatura,presion,tiempo", comments="")

print("✔ CSV sintético generado.")

# ===============================================================
# 2. Leer el CSV
# ===============================================================
df = pd.read_csv("datos_sinteticos.csv")
print("✔ CSV leído correctamente.")

# ===============================================================
# 3. Calcular estadísticas por columna
# ===============================================================
stats = df.describe()

# ===============================================================
# 4. Filtrar outliers (valores > 3σ)
# ===============================================================
df_filtered = df.copy()

for column in df.columns:
    mean = df[column].mean()
    std = df[column].std()
    lower = mean - 3 * std
    upper = mean + 3 * std

    df_filtered = df_filtered[
        (df_filtered[column] >= lower) & (df_filtered[column] <= upper)
    ]

print("✔ Outliers eliminados.")

# ===============================================================
# 5. Guardar CSV limpio y reporte
# ===============================================================
df_filtered.to_csv("datos_filtrados.csv", index=False)

with open("reporte.txt", "w") as f:
    f.write("=== REPORTE DE ESTADÍSTICAS ===\n\n")
    f.write(">> Estadísticas generales:\n")
    f.write(str(stats))
    f.write("\n\n>> Total de líneas originales: {}\n".format(len(df)))
    f.write(">> Total después de filtrar: {}\n".format(len(df_filtered)))
    f.write("\nProceso completado exitosamente.\n")

print("✔ Reporte generado y datos guardados.")

