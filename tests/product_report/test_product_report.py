# from inventory_report.inventory.product import Product
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    pass  # Seu teste deve ser escrito aqui
    product = Product(
        1,
        "Produto 1",
        "Empresa 1",
        "2018-06-06",
        "2025-08-22",
        "001",
        "em local Seguro",
    )

    assert product.__repr__() == (
        f"O produto { product.nome_do_produto }"
        f" fabricado em { product.data_de_fabricacao }"
        f" por { product.nome_da_empresa } com validade"
        f" até { product.data_de_validade }"
        f" precisa ser armazenado { product.instrucoes_de_armazenamento }."
    )
