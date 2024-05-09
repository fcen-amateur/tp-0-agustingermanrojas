"""
# TPcit0: una galería de _gapminder_
"""

import importlib
from pkgutil import iter_modules

from matplotlib.figure import Figure
import seaborn.objects as so
import plotters


def submodulos(modulo):
    return [submodule.name for submodule in iter_modules(modulo.__path__)]


def test_formato_plot():
    for nombre in submodulos(plotters):
        submodulo = importlib.import_module(f"plotters.{nombre}")
        assert "plot" in dir(submodulo), "La función `plot` no está en %s" % nombre
        retorno = submodulo.plot()
        assert isinstance(retorno, dict), "El retorno de `plot` debería ser un dict"
        assert set(retorno.keys()) == {"figura", "descripcion", "autor"}
        assert isinstance(retorno["figura"], (so.Plot, Figure)) or hasattr(
            retorno["figura"], "figure"
        ), "`figura` debe ser (a) un so.Plot, (b) una mpl.figure.Figure o (c) tener un attributo `figure` que sea una Figure"
        assert isinstance(retorno["autor"], str), "`autor` debe ser un str"
        assert isinstance(retorno["descripcion"], str), "`descripcion` debe ser un str"
