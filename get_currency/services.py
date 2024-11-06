import pandas as pd


def get_value(char_code='USD'):
    """ Получает текущий курс валюты в рублях, источник данных ЦБ РФ """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    data = pd.read_xml(url, encoding='cp1251')
    value = data.loc[data['CharCode'].isin([char_code]), ['Value']]
    return value.values[0][0]

