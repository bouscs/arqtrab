from typing import TypeVar, Generic


T = TypeVar('T')
S = TypeVar('S', bound=str)

# Classe genérica para repositórios de objetos
class Colecao(Generic[T, S]):
    def __init__(self):
        self.items: list[T] = []

    # Adiciona um elemento ao repositório e retorna True se a operação foi bem sucedida
    def adicionar(self, item: T):
        if (item in self.items):
            return False
        self.items.append(item)
        return True

    # Remove um elemento do repositório e retorna True se a operação foi bem sucedida
    def remover(self, item: T):
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    # Obter o primeiro elemento do repositório com o atributo especificado, ou None se não for encontrado
    def obter_um(self, atributo: S, valor: str):
        for item in self.items:
            if getattr(item, atributo) == valor:
                return item
        return None
