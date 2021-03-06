from scrap import make_html


@make_html('http://www.cucsur.udg.mx/directorio', 'div', 'item-list')
def cucsur_data(items):

    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': []
    }

    for item in items:

        li = item.find_all('li', 'views-row')

        for i in li:

            sub = i.find_all(class_='field-content')

            table['area'].append(item.h3.text)
            table['imagen'].append(sub[1].img['src'])
            table['nombre'].append(sub[2].a.text)
            table['puesto'].append(sub[3].text)
            table['direccion'].append(sub[4].text)
            table['telefono'].append(sub[5].text)

    return table, 'cucsur'
