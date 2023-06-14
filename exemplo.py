
from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

# Exemplo de uso do código:


# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
print(f"Livro criado com sucesso: {livro1.obter_titulo()}")
livro2 = Livro("Python Avançado", "Jane Doe", 2020)
print(f"Livro criado com sucesso: {livro2.obter_titulo()}")

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
print(f"Usuário {usuario1.obter_nome()} criado com sucesso")
usuario2 = Usuario("Bob", "bob@example.com")
print(f"Usuário {usuario2.obter_nome()} criado com sucesso")

# Criação da biblioteca
biblioteca = Biblioteca()
print("Biblioteca criada com sucesso")

# Adicionar livros à biblioteca
biblioteca.livros.adicionar(livro1)
print(f"\"{livro1.obter_titulo()}\" adicionado à biblioteca com sucesso")
biblioteca.livros.adicionar(livro2)
print(f"\"{livro2.obter_titulo()}\" adicionado à biblioteca com sucesso")

# Adicionar usuários à biblioteca
biblioteca.usuarios.adicionar(usuario1)
print(f"Usuário \"{usuario1.obter_nome()}\" adicionado à biblioteca com sucesso")
biblioteca.usuarios.adicionar(usuario2)
print(f"Usuário \"{usuario2.obter_nome()}\" adicionado à biblioteca com sucesso")

# Empréstimo de livro
biblioteca.emprestar(livro1, usuario1)
print(f"Livro \"{livro1.obter_titulo()}\" emprestado para \"{usuario1.obter_nome()}\" com sucesso")

# Tentativa de empréstimo de livro indisponível
try:
    biblioteca.emprestar(livro1, usuario2)
except Exception as e:
    print(e)

# Devolução de livro
biblioteca.devolver(livro1)
print(f"Livro \"{livro1.obter_titulo()}\" devolvido à biblioteca com sucesso")

# Remoção de livro
biblioteca.livros.remover(livro2)
print(f"Livro \"{livro2.obter_titulo()}\" removido da biblioteca com sucesso")

# Remoção de usuário
biblioteca.usuarios.remover(usuario2)
print(f"Usuário \"{usuario2.obter_nome()}\" removido da biblioteca com sucesso")

# Busca de livro e usuário
livro_encontrado = biblioteca.livros.obter_um("_titulo", "Python para Iniciantes")
usuario_encontrado = biblioteca.usuarios.obter_um("_nome", "Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.obter_titulo())
if usuario_encontrado:
    print(usuario_encontrado.obter_nome())
