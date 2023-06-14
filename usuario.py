class Usuario:
    _nome: str
    _email: str

    def __init__(self, nome: str, email: str):
        if not nome:
            raise Exception("Nome inválido")

        if not email:
            raise Exception("E-mail inválido")

        self._nome = nome
        self._email = email

    def obter_nome(self):
        return self._nome

    def obter_email(self):
        return self._email
