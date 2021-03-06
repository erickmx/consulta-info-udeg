from scrap import make_html


@make_html('http://www.cucei.udg.mx/es/directorio/', 'div', 'item-list')
def cucei_data(items):
    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': []
    }

    for i in items:
        table['area'].append(i.h3.text)
        table['nombre'].append(i.ul.li.a.text)
        sub = i.find_all('div', class_='field-content')
        table['imagen'].append(sub[0].img['src'])
        table['puesto'].append(sub[1].text)
        table['direccion'].append(sub[2].text)
        table['telefono'].append(sub[4].text)

    return table, 'cucei'
