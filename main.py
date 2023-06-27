import pandas as pd
from pprint import pprint
import json

class Handlerexcel:
    def __init__(self, file_1):
        self.file_1 = file_1
        # self.exel = pd.read_excel(self.file_1, usecols="E,G,L,M,AC,AF")

    def update_price(self):
        """
        Преобразует исходный спарешный exel файл в json Для заливки цен х2.2
        без знаков после точки
        :return:
        """
        excel = pd.read_excel(self.file_1, usecols="E,G")
        excel['Цена'] *= 2.2
        excel['Цена'] = excel['Цена'].astype(int)
        excel.rename(columns={'Артикул': 'nmId', 'Цена': 'price'}, inplace=True)
        excel.to_json('example_1.json', orient='records', lines=False)
        # with open('example_1.json', 'w') as f:

        return excel



if __name__ == '__main__':

    pattern = Handlerexcel('sima-land.ru_21-06-23_21-22-09-563.xlsx')
    result = pattern.update_price()
    pprint(result)  # проверка в терминале какие данные в json попадают

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
