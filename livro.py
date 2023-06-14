class Livro:
    _titulo: str
    _autor: str
    _ano_publicacao: str

    def __init__(self, titulo: str, autor: str, ano_publicacao: str):
        if not titulo:
            raise Exception("Título inválido")

        if not autor:
            raise Exception("Autor inválido")

        if not ano_publicacao:
            raise Exception("Ano de publicação inválido")

        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao

    def obter_titulo(self):
        return self._titulo

    def obter_autor(self):
        return self._autor

    def obter_ano_publicacao(self):
        return self._ano_publicacao
