#### Nombre del Proyecto
<h1 align="center" > DESARROLLO DE VISUALIZACIÓN DE DIFERENTES GRÁFICOS, UTILIZANDO LA LIBRERÍA MATPLOTLIB</h1>

#### Descripción del Proyecto
En este trabajo, implementaremos líneas de código para realizar las muestras de diferentes gráficos, utilizando nuestro archivo que es `pokemon.json`; de tal forma, para cumplir con la visualización de estos datos, requerimos de la librería matplotlib.
Vamos a graficar los puntos recomendados, como parte de la instruccion de este proyecto.

---
#### Datos de nuestro equipo

|INTEGRANTES DEL EQUIPO|ID DE GITHUB
| ------------- | ------------------------------ |
| Sofía Ximena Mucha Campos   |91231697|
| Luis Méndez Lázaro   |91269051|
| Mauricio Gabriel Gonzalez Kremer  |91268423 |
| Arnold JoaquínZevallos Dámazo  |91791428|


---
#### Instrucciones para ejecutar el proyecto

>**Las instrucciones son las siguientes:**
- Para poder mostrar el gráfico de barras, utilizamos la librería [matplotlib](https://matplotlib.org/ "matplotlib") y con las siguientes líneas de código: plt.bar(<keys>, <values>) plt.show(), podemos visualizar el gráfico. Keys serían los datos para el eje x, lo que para el ejercicio 1 sería los tipos de pokemon. Y en el eje y, los values, que sería la cantidad de pokemones, que tienen dicho tipo como una debilidad. Además, para guardar los datos utilizamos listas y diccionarios.
- En el ejercicio 2, para poder graficar el [scatterplot](https://www.statmethods.net/graphs/scatterplot.html "scatterplot") utilizamos las siguientes líneas de código: plt.scatter(altura, peso), plt.show(). También, utilizamos el siguiente código: `plt.xlabel` ("Altura (cm)"), `plt.ylabel`("Peso (kg)"), para darle etiquetas a los ejes x e y.
Además, originalmente los datos de las alturas estaban en metros y para este ejercicio se pedía mostrarlos en centímetros. Por lo tanto, para la conversión, primero se hizo un slicing al string de la altura. Luego, se convierte en un float para multiplicarlo por 100 y redondearlo a un decimal. También se convierte a float el dato del peso para que pueda ser graficado en el scatterplot.
- En la consigna 3, se quiso mostrar la ubicación de los pokemones que tengan un ID con un número primo, estos siendo luego representados por puntos en un [mapa](https://bit.ly/Grafico-Mapa "mapa") de la región de Kanto. El proceso de nuestro código es primero verificar los IDs primos, que tendrán un valor True para luego agregar dependiendo de si tienen coordenadas o no, ser agregados en una lista. Finalmente, con las coordenadas x e y son impresos en la imagen de Kanto.
- En la consigna 4, se utilizó un [Pie chart](https://bit.ly/Pie-Chart "Pie chart") para mostrar gráficamente el porcentaje de pokemones que eclosionaron de distintos tipos de huevos. Estos huevos pueden se de 2 km, de 5 km, de 10 km o en su defecto no eclosionaron de ninguno.  A continuación, se muestra un fragmento del código que define a nuestro gráfico de torta:  data es un array con el número de pokemones por categoría.
```
ax.pie(data, colors = colors, labels = labels, autopct = '%1.1f%%', radius = 3, center = (4, 4),
wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame = True)
```


---
#### REPORTES GRÁFICOS
**Ejercicio 1** - **GRÁFICO DE BARRAS**

![](https://i.ibb.co/dGQfV5n/grafico-de-barras.png)

**Ejercicio 2** - **GRÁFICO DE DISPERSIÓN**
  
![](https://i.ibb.co/93SCVv1/Dispersion.jpg)

**Ejercicio 3** - **GRÁFICO SOBRE UN MAPA**
  
![](https://i.ibb.co/XVrrsX5/Kantito.jpg)

**Ejercicio 4** - **GRÁFICO CIRCULAR**
  
![](https://i.ibb.co/dMQL8g2/Eggs.jpg)
