from scrap import make_html

# cualtos es totalmente diferente


@make_html('http://www.cualtos.udg.mx/directorio', 'p', None)
def cualtos_data(items):
    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': []
    }

    cad = items[3].text.split('\n')
    table['area'].append('Rectoría')
    table['puesto'].append(cad[1][2:])
    table['nombre'].append(cad[0])
    table['imagen'].append(items[1].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[2][2:])

    cad = items[6].text.split('\n')
    table['area'].append('Secretaria Particular')
    table['puesto'].append(cad[2][2:])
    table['nombre'].append(cad[1])
    table['imagen'].append(items[5].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[3][2:])

    cad = items[11].text.split('\n')
    table['area'].append('Unidad de Protocolo')
    table['puesto'].append(cad[1][2:])
    table['nombre'].append(cad[0])
    table['imagen'].append(items[9].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[2][2:])

    cad = items[15].text.split('\n')
    table['area'].append('Asuntos Jurídicos')
    table['puesto'].append(cad[1][2:])
    table['nombre'].append(cad[0])
    table['imagen'].append(items[13].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[2][2:])

    cad = items[19].text.split('\n')
    table['area'].append('Secretaría Académica')
    table['puesto'].append(cad[1][1:])
    table['nombre'].append(cad[0])
    table['imagen'].append(items[17].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[2][2:])

    cad = items[23].text.split('\n')
    table['area'].append('Secretaría Administrativa')
    table['puesto'].append(cad[1][2:])
    table['nombre'].append(cad[0])
    table['imagen'].append(items[21].img['src'])
    table['direccion'].append('Carretera a Yahualica, Km. 7.5 Tepatitlán de Morelos, Jalisco.')
    table['telefono'].append(cad[2][2:])

    return table, 'cualtos'
