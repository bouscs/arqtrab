from typing import Literal

from colecao import Colecao
from livro import Livro
from usuario import Usuario

class Biblioteca:
    livros: Colecao[Livro, Literal["titulo"]]
    usuarios: Colecao[Usuario, Literal["nome"]]
    locacoes: dict[Livro, Usuario]

    def __init__(self):
        self.livros = Colecao()
        self.usuarios = Colecao()
        self.locacoes = {}

    # Verifica se um livro está disponível para empréstimo
    def esta_disponivel(self, livro: Livro):
        return livro not in self.locacoes

    # Realiza o empréstimo de um livro para um usuário
    def emprestar(self, livro: Livro, usuario: Usuario):
        if livro not in self.livros.items:
            raise Exception("Livro não cadastrado")

        if usuario not in self.usuarios.items:
            raise Exception("Usuário não cadastrado")

        if not self.esta_disponivel(livro):
            raise Exception(
                f"Livro \"{livro.obter_titulo()}\" indisponível para empréstimo")

        self.locacoes[livro] = usuario

    # Realiza a devolução de um livro
    def devolver(self, livro: Livro):
        if livro not in self.livros.items:
            raise Exception("Livro não cadastrado")

        if self.esta_disponivel(livro):
            raise Exception("Livro não emprestado")

        del self.locacoes[livro]
