from scrap import make_html

# 'http://www.udg.mx/directorio/CUCS:-Centro-Universitario-de-Ciencias-de-la-Salud'


@make_html('http://www.cucs.udg.mx/directorio', 'div', 'item-list')
def cucs_data(items):
    # li views-row

    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': []
    }

    # lista de div.item-list
    for item in items:

        li = item.find_all('li', 'views-row')

        for i in li:

            sub = i.find_all(class_='field-content')

            table['area'].append(item.h3.text)
            table['puesto'].append(sub[1].h2.text)
            table['imagen'].append(
                sub[2].img['src'] if sub[2].img is not None else ''
            )
            table['nombre'].append(sub[3].a.text)
            table['direccion'].append(sub[4].text)
            table['telefono'].append(sub[5].text)

    return table


"""
@make_html('http://www.cucs.udg.mx/directorio', 'div', 'item-list')
def cucs_data(items):
    # li views-row

    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': [],
    }

    area = None
    puesto = None
    nombre = None
    img = None
    direccion = None
    telefono = None

    # lista de div.item-list
    for item in items:

        li = item.find_all('li', 'views-row')
        area = item.h3.text

        for i in li:

            table['area'].append(area)
            try:
                # strong.puesto-directorio > div.field-content > h2
                puesto = i.find('strong', class_='puesto-directorio').text
            except Exception as e:
                puesto = ''

            table['puesto'].append(puesto)

            try:
                # div.foto-directorio > div.field-content > img
                img = i.find('div', class_='foto-directorio').div.img['src']
            except Exception as e:
                img = ''

            table['imagen'].append(img)

            try:
                # strong.views-field-title > span.field-content > a
                nombre = i.find('strong', class_='views-field-title').text
            except Exception as e:
                nombre = ''

            table['nombre'].append(nombre)

            try:
                # div.direccion-directorio > div.field-content
                direccion = i.find('div', 'direccion-directorio').div.text
                direccion = direccion.split(': ')[1]
            except Exception as e:
                direccion = ''

            table['direccion'].append(direccion)

            try:
                # div.telefono-directorio > div.field-content
                telefono = i.find('div', 'telefono-directorio').div.text
                telefono = telefono.split(': ')[1]
            except Exception as e:
                telefono = ''

            table['telefono'].append(telefono)

    return table
"""

##############################################################################

"""
@make_html('http://www.cucs.udg.mx/directorio', 'li', 'views-row')
def cucs_data(items):
    print(len(items))
    table = {
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': [],
    }

    puesto = None
    nombre = None
    img = None
    direccion = None
    telefono = None

    for i in items:
        print("--" * 20)
        try:
            # strong.puesto-directorio > div.field-content > h2
            puesto = i.find('strong', class_='puesto-directorio').div.h2.text
        except Exception as e:
            puesto = ''

        table['puesto'].append(puesto)
        print(puesto)

        try:
            # div.foto-directorio > div.field-content > img
            img = i.find('div', class_='foto-directorio').div.img['src']
        except Exception as e:
            img = ''

        table['imagen'].append(img)
        print(img)

        try:
            # strong.views-field-title > span.field-content > a
            nombre = i.find('strong', class_='views-field-title').span.a.text
        except Exception as e:
            nombre = ''

        table['nombre'].append(nombre)
        print(nombre)

        try:
            # div.direccion-directorio > div.field-content
            direccion = i.find('div', 'direccion-directorio').div.text
            direccion = direccion.split(': ')[1]
        except Exception as e:
            direccion = ''

        table['direccion'].append(direccion)
        print(direccion)

        try:
            # div.telefono-directorio > div.field-content
            telefono = i.find('div', 'telefono-directorio').div.text
            telefono = telefono.split(': ')[1]
        except Exception as e:
            telefono = ''

        table['telefono'].append(telefono)
        print(telefono)

    return table
"""
