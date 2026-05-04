from abc import ABC, abstractmethod

class ICarrinhoRepository(ABC):

    @abstractmethod
    def adicionar(self, titulo: str):
        pass

    @abstractmethod
    def obter_todos(self) -> list:
        pass

    @abstractmethod
    def remover(self, titulo: str):
        pass

    @abstractmethod
    def esvaziar(self):
        pass