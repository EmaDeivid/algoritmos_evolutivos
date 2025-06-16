import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

with open("resultados.csv", "r", encoding="utf-8") as f:
    contenido = f.read()

bloques = contenido.strip().split("\n\n")

df_fitness = pd.read_csv(StringIO(bloques[0]))
df_resumen = pd.read_csv(StringIO(bloques[1]))
df_metricas = pd.read_csv(StringIO(bloques[2]))
df_muestra = pd.read_csv(StringIO(bloques[3]))

df_muestra.columns = df_muestra.columns.str.strip()


plt.figure(figsize=(8, 5))
sns.lineplot(data=df_fitness, x="Generación", y="Fitness", hue="Representación", marker="o")
plt.title("Evolución del Fitness por Generación")
plt.xlabel("Generación")
plt.ylabel("Fitness")
plt.grid(True)
plt.tight_layout()
plt.savefig("fitness_por_generacion.png")
plt.show()


import re

def extraer_notas(texto):
    if pd.isna(texto):
        return []
    return [float(nota) for nota in re.findall(r"\((\d+(?:\.\d+)?)\)", texto)]

df_muestra["Notas"] = df_muestra["AlumnosMuestra"].apply(extraer_notas)

df_notas_expandido = df_muestra.explode("Notas").dropna(subset=["Notas"])
df_notas_expandido["Notas"] = df_notas_expandido["Notas"].astype(float)

plt.figure(figsize=(8, 5))
sns.histplot(data=df_notas_expandido, x="Notas", hue="Representación", kde=True, bins=10)
plt.title("Histograma de Notas por Representación")
plt.xlabel("Notas")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_notas.png")
plt.show()


plt.figure(figsize=(8, 5))
sns.boxplot(data=df_resumen, x="Representación", y="Promedio")
plt.title("Distribución de Promedios por Representación")
plt.ylabel("Promedio por examen")
plt.tight_layout()
plt.savefig("boxplot_promedios.png")
plt.show()
