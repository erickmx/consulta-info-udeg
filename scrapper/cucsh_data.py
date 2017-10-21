# from scrap import make_html
from urllib import request
from bs4 import BeautifulSoup
from pandas import DataFrame

# 'http://www.udg.mx/directorio/CUCSH:-Centro-Universitario-de-Ciencias-Sociales-y-Humanidades'

pages = [
    'http://www.cucsh.udg.mx/directorio/dependencia/Rector%C3%ADa',
    'http://www.cucsh.udg.mx/directorio/dependencia/Secretar%C3%ADa%20Acad%C3%A9mica%20',
    'http://www.cucsh.udg.mx/directorio/dependencia/Secretar%C3%ADa%20Administrativa',
    'http://www.cucsh.udg.mx/directorio/dependencia/Divisi%C3%B3n%20de%20Estudios%20Hist%C3%B3ricos%20y%20Humanos%20',
    'http://www.cucsh.udg.mx/directorio/dependencia/Divisi%C3%B3n%20de%20Estudios%20Pol%C3%ADticos%20y%20Sociales',
    'http://www.cucsh.udg.mx/directorio/dependencia/Divisi%C3%B3n%20de%20Estudios%20Jur%C3%ADdicos',
    'http://www.cucsh.udg.mx/directorio/dependencia/Divisi%C3%B3n%20de%20Estudios%20de%20Estado%20y%20Sociedad%20',
    'http://www.cucsh.udg.mx/directorio/dependencia/Divisi%C3%B3n%20de%20Estudios%20de%20la%20Cultura%20',
    'http://www.cucsh.udg.mx/directorio/dependencia/Catedras'
]

table = {
    'area': [],
    'puesto': [],
    'nombre': [],
    'imagen': [],
    'direccion': [],
    'telefono': []
}


def cucsh_data():
    for page in pages:
        page_html = request.urlopen(page)
        soup = BeautifulSoup(page_html)
        items = soup.find_all('div', class_='item-list')

        area = None
        puesto = None
        nombre = None
        img = None
        direccion = None
        telefono = None

        for item in items:

            area = item.h3.text
            li = item.find_all('li', class_='views-row')

            for i in li:

                table['area'].append(area)

                try:
                    img = i.find('img', class_='image-directorio')['src']
                except Exception as e:
                    img = ''

                table['imagen'].append(img)

                try:
                    nombre = i.find('div', 'views-field-title').text
                except Exception as e:
                    nombre = ''

                table['nombre'].append(nombre)

                try:
                    puesto = i.find('div', 'views-field-field-puesto-dir-value').text
                    puesto = puesto.split(': ')[1]
                except Exception as e:
                    puesto = ''

                table['puesto'].append(puesto)

                try:
                    direccion = i.find('div', 'views-field-field-address-dir-value').text
                    direccion = direccion.split(': ')[1]
                except Exception as e:
                    direccion = ''

                table['direccion'].append(direccion)

                try:
                    telefono = i.find('div', 'views-field-field-telefono-dir-value').text
                    telefono = telefono.split(': ')[1]
                except Exception as e:
                    telefono = ''

                table['telefono'].append(telefono)

    html_file = 'cucsh.html'
    df = DataFrame(data=table, columns=table.keys())

    salida = open(html_file, 'w')
    salida.write(df.to_html())
    salida.close()
