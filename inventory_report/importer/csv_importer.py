from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path):
        type = path.split(".")[1]
        if type == "csv":
            with open(path) as file:
                dict_list = list(csv.DictReader(file))
            return dict_list
        else:
            raise ValueError("Arquivo inválido")
