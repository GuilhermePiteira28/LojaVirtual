# =====================
# Exceções Personalizadas
# =====================

class ProdutoInexistenteError(Exception):
    """Exceção para produto não encontrado na lista."""
    pass

class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente na tentativa de pagamento."""
    pass


# =====================
# Dados da Loja
# =====================

produtos = {
    "Camisola": 49.90 / 5,
    "calças": 89.90 / 5,
    "tênis": 199.90 / 5,
    "chapeu": 29.90 / 5
}

carrinho = {}
saldo_usuario = 300.00 / 5  # Saldo fictício para simulação em euros


# =====================
# Funções da Loja
# =====================

def listar_produtos():
    """Exibe todos os produtos disponíveis com nome e preço."""
    print("\nProdutos Disponíveis:")
    for nome, preco in produtos.items():
        print(f"- {nome.capitalize()} — € {preco:.2f}")


def adicionar_ao_carrinho():
    """Adiciona um produto ao carrinho com verificação de existência e quantidade válida."""
    try:
        produto = input("Digite o nome do produto: ").strip().lower()
        if produto not in produtos:
            raise ProdutoInexistenteError(f"'{produto}' não está disponível na loja.")

        quantidade = int(input("Digite a quantidade desejada: "))
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero.")

        carrinho[produto] = carrinho.get(produto, 0) + quantidade
        print(f"{quantidade}x '{produto}' adicionado(s) ao carrinho.")

    except ProdutoInexistenteError as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro positivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def visualizar_carrinho():
    """Exibe os itens do carrinho com valores totais."""
    print("\nSeu Carrinho:")
    if not carrinho:
        print("Carrinho vazio.")
        return

    total = 0
    for produto, quantidade in carrinho.items():
        preco_unitario = produtos[produto]
        subtotal = preco_unitario * quantidade
        total += subtotal
        print(f"{produto.capitalize()} x{quantidade} — € {subtotal:.2f}")

    print(f"Total da compra: € {total:.2f}")


def pagar():
    """Processa o pagamento simulando o uso de saldo e tratando erros como saldo insuficiente ou carrinho vazio."""
    global saldo_usuario
    try:
        if not carrinho:
            raise Exception("Não é possível pagar com o carrinho vazio.")

        total = sum(produtos[prod] * qtd for prod, qtd in carrinho.items())

        if total > saldo_usuario:
            raise SaldoInsuficienteError("Saldo insuficiente para completar a compra.")

        saldo_usuario -= total
        print(f"Pagamento realizado com sucesso! Valor pago: € {total:.2f}")
        print(f"Saldo restante: € {saldo_usuario:.2f}")
        carrinho.clear()

    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("Operação finalizada.")


def exibir_menu():
    """Exibe o menu principal e gerencia a navegação do usuário."""
    while True:
        print("\n========= MENU Loja Virtual =========")
        print("1. Listar produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Visualizar carrinho")
        print("4. Pagar")
        print("5. Sair")
        print("========================")

        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            match opcao:
                case 1:
                    listar_produtos()
                case 2:
                    adicionar_ao_carrinho()
                case 3:
                    visualizar_carrinho()
                case 4:
                    pagar()
                case 5:
                    print("Saindo da loja. Até logo!")
                    break
                case _:
                    print("Opção inválida. Escolha entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 5.")


# =====================
# Execução do Sistema
# =====================

if __name__ == "__main__":
    print("Bem-vindo à Loja Virtual")
    exibir_menu()
