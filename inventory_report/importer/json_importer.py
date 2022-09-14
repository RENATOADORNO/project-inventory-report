from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path):
        type = path.split(".")[1]
        if type == "json":
            with open(path) as file:
                dict_list = json.loads(file.read())
            return dict_list
        else:
            raise ValueError("Arquivo inválido")
