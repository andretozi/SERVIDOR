from domain.interfaces import ICarrinhoRepository

class CarrinhoUseCase:
    def __init__(self, repositorio: ICarrinhoRepository):
        self.repositorio = repositorio

    def adicionar_livro(self, titulo):
        self.repositorio.adicionar(titulo)

    def listar_carrinho(self):
        return self.repositorio.obter_todos()

    def remover_livro(self, titulo):
        self.repositorio.remover(titulo)

    def limpar_carrinho(self):
        self.repositorio.esvaziar()