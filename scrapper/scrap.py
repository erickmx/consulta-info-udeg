from urllib import request
from bs4 import BeautifulSoup
import pandas


# decorador que recibe parametros
def make_html(page_url, tag_name, tag_class):

    # decorador interno que usa los parametros
    def _make_html(func):
        page = request.urlopen(page_url)
        soup = BeautifulSoup(page)
        _items = soup.find_all(tag_name, class_=tag_class)

        # nueva funcion
        def make_table(items=_items):
            table = {}

            # ejecucion de la funcion definida
            table, html_name = func(items)

            html_file = '{}.html'.format(html_name)
            df = pandas.DataFrame(data=table, columns=table.keys())

            salida = open(html_file, 'w')
            salida.write(df.to_html())
            salida.close()

        return make_table

    return _make_html
