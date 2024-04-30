"""
# TPcit0: una galería de _gapminder_
"""

import streamlit as st
from  matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn.objects as so
import importlib
import plotters
from pkgutil import iter_modules


def submodulos(modulo):
    return [submodule.name for submodule in iter_modules(modulo.__path__)]

# st.set_page_config(layout="wide")
st.write("# TPcit0: una galería de _gapminder_")


opcion = st.selectbox("¿Qué gráfico desea ver?", submodulos(plotters))

data = importlib.import_module(f"plotters.{opcion}").plot()

if isinstance(data, so.Plot) or isinstance(data, Figure):
    data = dict(autor="N/A", descripcion="No disponible", figura=data)

fig = plt.figure(figsize=(11,6))
if isinstance(data["figura"], so.Plot):
    data["figura"].on(fig).show()
elif isinstance(data["figura"], Figure):
    fig = data["figura"]
else:
    fig.text(0.5, 0.5, "Figura no disponible", fontsize=20, ha="center")

st.write("### Descripción\n", data["descripcion"])
st.write("#### Autor(es)\n", data["autor"])
st.pyplot(fig)
