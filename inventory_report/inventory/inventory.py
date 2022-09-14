import csv
import json
from xml.etree import ElementTree
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        if path.endswith(".csv"):
            return Inventory.read_csv(path, report_type)
        elif path.endswith(".json"):
            if report_type == "simples":
                return simple_report.generate(Inventory.read_json(path))
            return complete_report.generate(Inventory.read_json(path))

        if report_type == "simples":
            return simple_report.generate(Inventory.read_xml(path))
        return complete_report.generate(Inventory.read_xml(path))

    @classmethod
    def read_csv(cls, path, report_type):
        simple_report = SimpleReport
        complete_report = CompleteReport
        dict_list = list()
        with open(path) as file:
            dict_list = list(csv.DictReader(file))
        if report_type == "simples":
            return simple_report.generate(dict_list)
        return complete_report.generate(dict_list)

    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            return json.load(file)

    @classmethod
    def read_xml(cls, path):
        tree = ElementTree.parse(path)
        roots = list(tree.getroot())
        dict_list = []
        prod_dict = {}

        for index in range(len(roots)):
            for prod in roots[index]:
                prod_dict[prod.tag] = prod.text
            dict_list.append(prod_dict)
            prod_dict = {}
        return dict_list
