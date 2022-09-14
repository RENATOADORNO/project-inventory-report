from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    def generate(data):
        simple_report = SimpleReport.generate(data)

        data_list = Counter([product["nome_da_empresa"] for product in data])
        quantity = ""

        for factory in data_list:
            quantity += f"- {factory}: {data_list[factory]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{quantity}"
        )
