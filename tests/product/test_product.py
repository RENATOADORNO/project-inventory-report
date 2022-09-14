from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Produto 1",
        "Empresa 1",
        "2018-06-06",
        "2025-08-22",
        "001",
        "Armazenar em local Seguro",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto 1"
    assert product.nome_da_empresa == "Empresa 1"
    assert product.data_de_fabricacao == "2018-06-06"
    assert product.data_de_validade == "2025-08-22"
    assert product.numero_de_serie == "001"
    assert product.instrucoes_de_armazenamento == "Armazenar em local Seguro"
