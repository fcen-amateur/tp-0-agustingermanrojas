import seaborn.objects as so
from gapminder import gapminder
import matplotlib as mpl
import matplotlib.lines as mlines


def plot():

    # Carga de datos
    df = gapminder
    countries = ['Iran','Iraq']
    df_filtered = df[df['country'].isin(countries)]
    df1 = df_filtered.groupby(['year', 'country'])['lifeExp'].mean().reset_index()
    df2 = df_filtered.groupby(['year', 'country'])['gdpPercap'].mean().reset_index()
    df1['gdpPercap'] = df2['gdpPercap']/1000
    df = df1

    # Paleta
    color1 = '#f1f1f1'
    color2 = '#239F40'
    color3 = '#000000'

    # Gráfico
    p= (
    so.Plot(df, x='year').pair(y=['gdpPercap','lifeExp'])
    .add(so.Line(marker='o',pointsize=3.5, color='green'), data=df[df['country']=='Iran']
        )
    .add(so.Line(marker='o',pointsize=3.5, color='black'), data=df[df['country']=='Iraq']
        )
    .label(
        ).label(x='Años', y0='Miles de dólares', y1='Años de vida')
        .theme({'axes.facecolor': 'w', 'axes.edgecolor': color1}) 
    )

    # .on
    f = mpl.figure.Figure()
    res = p.on(f).plot()
    ax0 = f.axes[0]
    ax1 = f.axes[1]

    # Años de guerra
    ax0.axvspan(xmin=1980, xmax=1989, color=color1, alpha=0.5)
    ax1.axvspan(xmin=1980, xmax=1989, color=color1, alpha=0.5)

    # Títulos
    f.suptitle('Impacto de la Guerra Impuesta 1980-1989', fontsize=14)
    ax0.set_title('Evolución del PBI per cápita', fontsize=11)
    ax1.set_title('Evolución de la expectativa de vida', fontsize=11)

    # Leyenda
    line_iran = mlines.Line2D([], [], color=color2, label='Iran')
    line_iraq = mlines.Line2D([], [], color=color3, label='Iraq')
    ax0.add_line(line_iran)
    ax0.add_line(line_iraq)
    ax0.legend(loc='upper left', ncol=2, frameon=False)

    # Ajustes de tamaño
    current_size = f.get_size_inches()
    f.set_size_inches(current_size[0] * 1.5, current_size[1] * 1.5)

    figura = f

    return dict(
        descripcion='El gráfigo muestra el impacto de la Guerra Impuesta (1980-1989) entre Irán e Irak, medido en base al PBI per cápita y la expectativa de vida de cada país. Se observa la evolución de las variables desde 28 años antes y hasta 18 años después.\n \n Millones de personas sufrieron debido a los combates, ataques aéreos y el uso de armas químicas. A pesar de los esfuerzos de mediación internacional, la guerra terminó sin un claro ganador y dejó secuelas duraderas en ambas naciones.',
        autor='Agustín Rojas',
        figura=figura,
    )
