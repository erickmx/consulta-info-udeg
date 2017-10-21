from scrap import make_html


# @make_html(
#     'http://www.udg.mx/directorio/CUAAD:-Centro-Universitario-de-Arte,-Arquitectura-y-Dise%C3%B1o',
#     'div',
#     'item-list'
# )
@make_html('http://www.cuaad.udg.mx/?q=directorio', 'div', 'dir_contacto')
def cuaad_data(items):
    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': []
    }

    for item in items:

        p = item.find_all('p')

        for i in p:
            pass

            # sub = i.find_all(class_='field-content')
            # print('--' * 20)
            # print(sub)

            # table['area'].append(item.h3.text)
            # table['puesto'].append(sub[1].h2.text)
            # table['imagen'].append(
            #     sub[2].img['src'] if sub[2].img is not None else ''
            # )
            # table['nombre'].append(sub[3].a.text)
            # table['direccion'].append(sub[4].text)
            # table['telefono'].append(sub[5].text)

    return table
