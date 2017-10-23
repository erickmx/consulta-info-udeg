from scrap import make_html


# @make_html('http://www.cuaad.udg.mx/?q=directorio', 'div', 'dir_contacto')
@make_html(
    'http://www.udg.mx/directorio/CUAAD:-Centro-Universitario-de-Arte,-Arquitectura-y-Dise%C3%B1o',
    'div',
    'item-list'
)
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

        li = item.find_all('li', 'views-row')

        for i in li:

            if item.h3 is not None:
                table['area'].append(item.h3.text)

            if i is not None:

                puesto = i.find(class_='puesto-directorio')
                nombre = i.find(class_='views-field-title')
                img = i.find(class_='foto-directorio')
                direccion = i.find(class_='direccion-directorio')
                telefono = i.find(class_='telefono-directorio')

                if puesto is not None:
                    table['puesto'].append(puesto.text)

                if nombre is not None:
                    table['nombre'].append(nombre.text)

                if img is not None:
                    table['imagen'].append(img.img['src'])

                if direccion is not None:
                    table['direccion'].append(direccion.text)

                if telefono is not None:
                    table['telefono'].append(telefono.text)

    return table, 'cuaad'
