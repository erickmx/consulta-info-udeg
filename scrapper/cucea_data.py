from scrap import make_html


@make_html(
    'http://www.cucea.udg.mx/es/acerca-de-cucea/directorio',
    'div',
    'item-list'
)
def cucea_data(items):

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
            table['imagen'].append(sub[1].img['src'])
            table['nombre'].append(sub[2].a.text)
            table['puesto'].append(sub[3].text)
            table['direccion'].append(sub[4].text)
            table['telefono'].append(sub[5].text)

    return table, 'cucea'
