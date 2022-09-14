from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


MOCK_LIST = [
    {
        "id": "1",
        "nome_do_produto": "Steak de Frango Sadia 100g",
        "nome_da_empresa": "Sadia",
        "data_de_fabricacao": "2021-05-01",
        "data_de_validade": "2023-06-02",
        "numero_de_serie": "23091827391827631",
        "instrucoes_de_armazenamento": "Manter em local gelado",
    },
    {
        "id": "2",
        "nome_do_produto": "Tang Sabor Laranja",
        "nome_da_empresa": "Mondelēz International",
        "data_de_fabricacao": "2022-06-15",
        "data_de_validade": "2023-07-15",
        "numero_de_serie": "36128736192873162",
        "instrucoes_de_armazenamento": "Manter em local arejado",
    },
    {
        "id": "3",
        "nome_do_produto": "Tang Sabor Uva",
        "nome_da_empresa": "Mondelēz International",
        "data_de_fabricacao": "2022-06-15",
        "data_de_validade": "2023-07-15",
        "numero_de_serie": "92387120983712937",
        "instrucoes_de_armazenamento": "Manter em local arejado",
    },
]


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport)

    send_report = report.generate(MOCK_LIST)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in send_report
    assert "\033[36m2021-05-01\033[0m" in send_report
    assert "\033[32mData de validade mais próxima:\033[0m" in send_report
    assert "\033[36m2023-06-02\033[0m" in send_report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in send_report
    assert "\033[31mMondelēz International\033[0m" in send_report
