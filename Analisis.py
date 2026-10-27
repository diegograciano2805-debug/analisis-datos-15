import pandas as pd
import numpy as np

# 1. Cargar el dataset
file_name = 'billboard_hot_100_spotify_audio_features_enriched.csv'
print("Cargando dataset...")
df = pd.read_csv(file_name)

# 2. Exploración y verificación de registros (mínimo 15,000)
print(f"Total de registros iniciales: {len(df)}")
print("\nPrimeras 5 filas:")
print(df.head())

# 3. Limpieza de Datos
# Eliminar filas duplicadas
df = df.drop_duplicates()

# Manejar valores nulos (puedes ajustar según las columnas)
df_limpio = df.dropna()
print(f"\nTotal de registros después de limpiar nulos y duplicados: {len(df_limpio)}")

# 4. Cálculo de Estadísticos Descriptivos
print("\n=== ESTADÍSTICOS DESCRIPTIVOS (MEDIAS, MEDIANAS, MODAS, DESVIACIÓN ESTÁNDAR) ===")

# Seleccionar solo columnas numéricas (duración, danceability, energy, loudness, etc.)
columnas_numericas = df_limpio.select_dtypes(include=[np.number])

# Medias
medias = columnas_numericas.mean()

# Medianas
medianas = columnas_numericas.median()

# Modas (tomamos el primer valor si hay múltiples)
modas = columnas_numericas.mode().iloc[0]

# Desviaciones estándar
desviaciones = columnas_numericas.std()

# Crear un DataFrame resumen
resumen_estadistico = pd.DataFrame({
    'Media': medias,
    'Mediana': medianas,
    'Moda': modas,
    'Desviación Estándar': desviaciones
})

print(resumen_estadistico)

# 5. Exportar el dataset limpio para importar en Power BI
output_file = 'dataset_limpio.csv'
df_limpio.to_csv(output_file, index=False)
print(f"\n¡Dataset limpio guardado exitosamente como '{output_file}'!")