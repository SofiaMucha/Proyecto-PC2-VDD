import matplotlib.pyplot as plt
import numpy as np
from aux_functions import getAllPokemons, getPokemonByName,getLocationsByName, getTypesByName, getWeaknessesByName
#CREAR UN GRÁFICO DE BARRAS EN EL CUAL SE MUESTRE LOS TIPOS DE POKEMON EN EL EJE X, Y LA CANTIDAD DE POKEMONES QUE TIENEN DICHO TIPO COMO UNA DEBILIDAD EN EL EJE Y

todos = []
types = []

pokemones = getAllPokemons()
todos_name = []
for i in range(len(pokemones)):
    a = pokemones[i]["type"]
    for j in range(len(a)):
        todos.append(a[j])
        if a[j] not in types:
            types.append(a[j])

for i in range(len(pokemones)):
    a = pokemones[i]["name"]
    if a not in todos_name:
        todos_name.append(a)
typos = {}
for i in range(len(types)):
    typos[types[i]] = 0

debilidades = []
for i in range(len(todos_name)):
    debilidades = getWeaknessesByName(todos_name[i])
    for j in range(len(debilidades)):
        if debilidades[j] in list(typos.keys()):
            typos[debilidades[j]] += 1

claves = []
valores = []
for key,value in typos.items():
    claves.append(key)
    valores.append(value)
colors = ['red', 'blue', 'yellow', 'green', 'orange','indigo','lightcoral','goldenrod','turquoise'
        ,'violet','sienna','lightgreen','khaki','lavender','lemonchiffon']
plt.bar(claves, valores, color=colors)
plt.show()

#CREAR UN SCATTERPLOT EN EL CUAL SE MUESTRE LA ALTURA DE LOS POKEMONES EN CENTÍMETROS EN EL EJE X, Y EL PESO DE LOS POKEMONES EN KG EN EL EJE Y.
altura = []
peso = []
for i in range(len(pokemones)):
    a = pokemones[i]["height"]
    a = round(float(a[:4])*100, 1)
    b = pokemones[i]["weight"]
    b = float(b[:4])
    altura.append(a)
    peso.append(b)

plt.scatter(altura, peso)
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.show()

#MOSTAR EN EL MAPA DE KANTO.PNG LA UBICACIÓN DE TODOS LOS POKEMONS CUYO ID ES UN NÚMERO PRIMO. EL CÁLCULO O VERIFICACIÓN DE SI EL NÚMERO ES PRIMO DEBE REALIZARSE EN CÓDIGO, EN OTRAS PALABRAS, NO SERÁ ACEPTABLE QUE OBTENGA LOS POKEMONS CON ID PRIMO DE MANERA MANUAL.

def primeCheck(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


pkmnLocation = []

pokedex = getAllPokemons()
for n in range(len(pokedex)):
    if primeCheck(pokedex[n]["id"]) == True:
        if "coordx" in pokedex[n]:
            pkmnLocation.append(pokedex[n])

im = plt.imread('Kanto.png')
plt.imshow(im)

for i in range(len(pkmnLocation)):
    for j in range(len(pkmnLocation[i]["coordx"])):
        x = pkmnLocation[i]["coordx"][j]
        y = pkmnLocation[i]["coordy"][j]
        plt.plot(x, y, "o", c="black", markersize=5)
plt.show()
#GRÁFICO DE LIBRE ELECCIÓN. UTILICE ALGUNO DE LOS GRÁFICOS NO UTILIZADOS EN EL CURSO DE LA LIBRERIA MATPLOTLIB PARA MOSTRAR INFORMACIÓN QUE USTED CONSIDERE RELEVANTE DE LOS POKEMONES.

def GetEggsInfo():
    pokedex = getAllPokemons()
    CountNotEggs, Count10km, Count5km, Count2km = 0,0,0,0

    for pokemon in pokedex:
        if pokemon["egg"] == "Not in Eggs ":
            CountNotEggs += 1
        elif pokemon["egg"] == "10 km":
            Count10km += 1
        elif pokemon["egg"] == "5 km":
            Count5km += 1
        elif pokemon["egg"] == "2 km":
            Count2km += 1

    data = [CountNotEggs, Count10km, Count5km, Count2km]
    labels = ["Not in Eggs","10 km","5 km", "2 km"]
    colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, len(data)))

    fig, ax = plt.subplots()
    ax.pie(data, colors = colors, labels = labels, autopct = '%1.1f%%', radius = 3, center = (4, 4), 
            wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame = True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()
