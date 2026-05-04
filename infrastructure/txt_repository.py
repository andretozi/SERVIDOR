import os
from domain.interfaces import ICarrinhoRepository
from infrastructure.biblioteca_db import biblioteca

class CarrinhoTXTRepository(ICarrinhoRepository):

    def __init__(self, arquivo='carrinho.txt'):
        self.arquivo = arquivo
        if not os.path.exists(self.arquivo):
            open(self.arquivo, 'w', encoding='utf-8').close()

    def adicionar(self, titulo: str):
        with open(self.arquivo, 'a', encoding='utf-8') as f:
            f.write(titulo + '\n')

    def obter_todos(self) -> list:
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            titulos = [linha.strip() for linha in f.readlines() if linha.strip()]

        itens = []
        for t in titulos:
            for livro in biblioteca:
                if livro['titulo'] == t:
                    itens.append(livro)
                    break
        return itens

    def remover(self, titulo: str):
        with open(self.arquivo, 'r', encoding='utf-8') as f:
            titulos = [linha.strip() for linha in f.readlines() if linha.strip()]

        if titulo in titulos:
            titulos.remove(titulo)

        with open(self.arquivo, 'w', encoding='utf-8') as f:
            for t in titulos:
                f.write(t + '\n')


    def esvaziar(self):
        open(self.arquivo, 'w', encoding='utf-8').close()