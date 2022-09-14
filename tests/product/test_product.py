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
    assert product.nome_do_produto == "Todynho 200ml"
    assert product.nome_da_empresa == "PepsiCo"
    assert product.data_de_fabricacao == "2022-06-16"
    assert product.data_de_validade == "2023-08-15"
    assert product.numero_de_serie == "87340918374189237"
    assert product.instrucoes_de_armazenamento == "Conservar em local seco."
