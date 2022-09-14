from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    if len(sys.argv) != 3:
        return print("Verifique os argumentos", file=sys.stderr)
    path = sys.argv[1]
    type = sys.argv[2]
    file_type = path.split(".")[1]

    if file_type == "csv":
        inventory_refactor = InventoryRefactor(CsvImporter)
        return sys.stdout.write(
            inventory_refactor.import_data(path, type)
        )

    if file_type == "json":
        inventory_refactor = InventoryRefactor(JsonImporter)
        return sys.stdout.write(
            inventory_refactor.import_data(path, type)
        )

    if file_type == "xml":
        inventory_refactor = InventoryRefactor(XmlImporter)
        return sys.stdout.write(
            inventory_refactor.import_data(path, type)
        )

    raise ValueError()
