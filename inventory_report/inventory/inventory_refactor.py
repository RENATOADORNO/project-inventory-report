from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, Importer):
        self.importer = Importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type):
        self.data += self.importer.import_data(path)
        if type == "simples":
            return SimpleReport.generate(self.data)
        if type == "completo":
            return CompleteReport.generate(self.data)
        raise ValueError("Import data error")
