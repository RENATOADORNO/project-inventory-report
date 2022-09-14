from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Todynho 200ml",
        "PepsiCo",
        "2022-06-16",
        "2023-08-15",
        "87340918374189237",
        "Conservar em local seco.",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Monitor"
    assert product.nome_da_empresa == "Teclado"
    assert product.data_de_fabricacao == "2018-06-06"
    assert product.data_de_validade == "2025-08-22"
    assert product.numero_de_serie == "001"
    assert product.instrucoes_de_armazenamento == "Armazenar em local Seguro"
