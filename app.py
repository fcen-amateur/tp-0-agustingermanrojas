"""
# TPcit0: una galería de _gapminder_
"""

import streamlit as st
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn.objects as so
import importlib
import plotters
from pkgutil import iter_modules


def submodulos(modulo):
    return [submodule.name for submodule in iter_modules(modulo.__path__)]


# st.set_page_config(layout="wide")
st.write("# TPcit0: una galería de _gapminder_")


opcion = st.selectbox("¿Qué gráfico desea ver?", sorted(submodulos(plotters)))

data = importlib.import_module(f"plotters.{opcion}").plot()

if isinstance(data, (so.Plot, Figure)) or hasattr(data, "figure"):
    data = dict(autor="N/A", descripcion="No disponible", figura=data)

figura = data["figura"]
fig = plt.figure()
if isinstance(figura, so.Plot):
    figura.on(fig).show()
elif isinstance(figura, Figure):
    fig = figura
else:
    try:
        fig = figura.figure
    except AttributeError:
        fig.text(0.5, 0.5, "Figura no disponible", fontsize=20, ha="center")

st.write("### Descripción\n", data["descripcion"])
st.write("#### Autor(es)\n", data["autor"])
st.pyplot(fig)
