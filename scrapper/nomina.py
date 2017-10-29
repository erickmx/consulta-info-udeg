import requests
from bs4 import BeautifulSoup
from scrap import make_html
from unicodedata import category, normalize


def normalize_text(s):
    return ''.join(
        (c for c in normalize('NFD', s)
            if category(c) != 'Mn')
    )


def split_name(name):
    aux = name.split(' ')
    first_name = aux[0]
    if aux[-1] is not '':
        last_name1 = aux[-2]
        last_name2 = aux[-1]
    else:
        last_name1 = aux[-3]
        last_name2 = aux[-2]

    if 'ñ' not in first_name:
        first_name = normalize_text(first_name)
    if 'ñ' not in last_name1:
        last_name1 = normalize_text(last_name1)
    if 'ñ' not in last_name2:
        last_name2 = normalize_text(last_name2)

    return first_name, last_name1, last_name2


def nomina_udg(nombre, ap1, ap2):
    parametros = {
        "pPaterno": ap1.upper().encode('iso-8859-1'),
        "pMaterno": ap2.upper().encode('iso-8859-1'),
        "pNombre": nombre.upper().encode('iso-8859-1'),
        "pDepen": "",
        "pDepenDesc": "",
        "pTabu": "",
        "p_selMonto": "0",
        "p_selMes": "201710",
        "p_selQui": "1"
    }
    url = 'http://148.202.105.181/transd/ptqnomi_responsive.PTQNOMI_D'
    pagina = requests.get(url, params=parametros)
    soup = BeautifulSoup(pagina.content)
    td = soup.find_all(
        'td',
        # class_='td_beige',
        attrs={'data-title': 'SUELDO NETO'}
    )
    print('----' * 20)
    total = []
    for t in td:
        if t is not None:
            total.append(t.text)
        else:
            total.append('0.00')
    return total
    print(pagina.url)


def check_nomina(name_list=[]):
    list_salarios = []
    complete_name = ''
    first_name = ''
    last_name1 = ''
    last_name2 = ''
    salario = []

    for user in name_list:
        complete_name = user.split('. ')[-1]

        first_name, last_name1, last_name2 = split_name(complete_name)

        salario = nomina_udg(first_name, last_name1, last_name2)

        print(complete_name)
        print(salario)
        print('----' * 20)
        list_salarios.append(salario)

    return list_salarios


@make_html('http://www.cucei.udg.mx/es/directorio/', 'div', 'item-list')
def cucei_data(items):
    table = {
        'area': [],
        'puesto': [],
        'nombre': [],
        'imagen': [],
        'direccion': [],
        'telefono': [],
        'salario': []
    }

    for i in items:
        table['area'].append(i.h3.text)
        table['nombre'].append(i.ul.li.a.text)
        sub = i.find_all('div', class_='field-content')
        table['imagen'].append(sub[0].img['src'])
        table['puesto'].append(sub[1].text)
        table['direccion'].append(sub[2].text)
        table['telefono'].append(sub[4].text)

    table['salario'] = check_nomina(table['nombre'])

    return table, 'cucei'


cucei_data()

# print(normalize_text('córcholisñÑ'))
