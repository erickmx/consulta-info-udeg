from scrap import make_html


@make_html(
    'http://www.cunorte.udg.mx/acerca-de/directorio',
    'div',
    'item-list'
)
def cunorte_data(items):

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

            sub = i.find_all(class_='views-field')

            table['area'].append(item.h3.div.text)
            table['imagen'].append(sub[1].img['src'])
            table['nombre'].append(sub[2].a.text)
            table['puesto'].append(item.h3.div.text)
            table['direccion'].append(
                'Carretera Federal No. 23, Km. 191, 46200 Colotlán, Jal.'
            )
            table['telefono'].append(sub[4].text + sub[5].text)

    return table
