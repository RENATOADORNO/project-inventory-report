from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


MOCK = [
    {
        "id": "1",
        "nome_do_produto": "Produto 1",
        "nome_da_empresa": "Empresa 1",
        "data_de_fabricacao": "2021-05-01",
        "data_de_validade": "2023-06-02",
        "numero_de_serie": "001",
        "instrucoes_de_armazenamento": "Armazenar em local seguro",
    },
    {
        "id": "2",
        "nome_do_produto": "Produto 2",
        "nome_da_empresa": "Internacional",
        "data_de_fabricacao": "2022-06-15",
        "data_de_validade": "2023-07-15",
        "numero_de_serie": "002",
        "instrucoes_de_armazenamento": "Armazenar em local frio",
    },
    {
        "id": "3",
        "nome_do_produto": "Produto 3",
        "nome_da_empresa": "Internacional",
        "data_de_fabricacao": "2022-06-15",
        "data_de_validade": "2023-07-15",
        "numero_de_serie": "003",
        "instrucoes_de_armazenamento": "Armazenar em local quente",
    },
]


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport)

    send_report = report.generate(MOCK)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in send_report
    assert "\033[36m2021-05-01\033[0m" in send_report
    assert "\033[32mData de validade mais próxima:\033[0m" in send_report
    assert "\033[36m2023-06-02\033[0m" in send_report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in send_report
    assert "\033[31mInternacional\033[0m" in send_report
