import urllib.request
from bs4 import BeautifulSoup
import pandas

'''
Pandas sirve para crear dataframes o hojas de datos
'''

"""
cucei = 'http://www.cucei.udg.mx/es/directorio/'

# print(pagina)
pagina = urllib.request.urlopen(cucei)

soup = BeautifulSoup(pagina)

# print(soup)

items = soup.find_all('div',class_ = 'item-list')
# len(items)

# print(items[0].h3.string)
# print(items[2].h3.string)

sup = items[0].find_all('div',class_ = 'field-content')
# len(sup)

sup[0].img['src']
sup[1].text

for s in sup:
    print(s)

items[0].ul.li.a.text

for i in items:
    print(i.ul.li.a.text.split('.')[1])

"""

cucei = 'http://www.cucei.udg.mx/es/directorio/'

pagina = urllib.request.urlopen(cucei)

soup = BeautifulSoup(pagina)

items = soup.find_all('div', class_='item-list')

puestos = []
nombres = list()
imagenes = []
direcciones = []
telefonos = []

"""
for i in items:
    print(i.h3.text)
    print(i.ul.li.a.text.split('. ')[1])
    sub = i.find_all('div',  class_ = 'field-content' )

    print(sub[0].img['src'])
    print(sub[2].text)
    print(sub[4].text)
    #print(sub[6])
"""

for i in items:
    puestos.append(i.h3.text)
    nombres.append(i.ul.li.a.text)
    sub = i.find_all('div',  class_='field-content')

    imagenes.append(sub[0].img['src'])
    direcciones.append(sub[2].text)
    telefonos.append(sub[4].text)
    # print(sub[6])

df = pandas.DataFrame(puestos, columns=['puestos'])
df['nombre'] = nombres
df['imagen'] = imagenes
df['direccion'] = direcciones
df['telefono'] = telefonos

# print(df)

salida = open('cucei.html', 'w')
salida.write(df.to_html())
salida.close()

"""
for n in range(0,6,2):
    print(n)
"""
