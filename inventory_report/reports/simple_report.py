import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, data):
        manufacturing_date_list = list()
        expiration_date_list = list()
        factories_list = list()

        for product in data:
            if str(datetime.date.today()) > product["data_de_fabricacao"]:
                manufacturing_date_list.append(product["data_de_fabricacao"])

            if product["data_de_validade"] >= str(datetime.date.today()):
                expiration_date_list.append(product["data_de_validade"])

            factories_list.append(product["nome_da_empresa"])

        factories_counted = dict(Counter(factories_list).most_common(1))
        most_common_factory = list(factories_counted.keys())[0]

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date_list)}\n"
            f"Data de validade mais próxima: {min(expiration_date_list)}\n"
            f"Empresa com mais produtos: {most_common_factory}"
        )
