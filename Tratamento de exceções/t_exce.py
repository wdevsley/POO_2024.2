#Wesley Silva Araújo (2023010487)

class ErroLivroIndisponivel(Exception):
    def __init__(self, titulo, motivo):
        super().__init__(f"O livro '{titulo}' não está disponível: {motivo}.")
        self.titulo = titulo
        self.motivo = motivo

class ErroDevolucaoInvalida(Exception):
    def __init__(self, usuario, titulo):
        super().__init__(f"{usuario} tentou devolver '{titulo}', mas não possui esse empréstimo.")
        self.usuario = usuario
        self.titulo = titulo

class ErroEmprestimoAtrasado(Exception):
    def __init__(self, usuario, titulo, dias_atraso):
        multa = dias_atraso * 2.50
        super().__init__(f"{usuario} atrasou a devolução de '{titulo}' em {dias_atraso} dias. Multa de R${multa:.2f} aplicada.")
        self.usuario = usuario
        self.titulo = titulo
        self.dias_atraso = dias_atraso
        self.multa = multa

class Biblioteca:
    def __init__(self):
        self.livros = {"Python Essencial": True, "Aprendendo Machine Learning": True, "Dominando Python": True}
        self.emprestimos = {}
        self.reservas = {}
    
    def emprestar(self, usuario, titulo):
        if not isinstance(titulo, str):
            raise TypeError("O título do livro deve ser um texto válido.")
        if titulo in self.reservas:
            raise ErroLivroIndisponivel(titulo, "reservado para outro usuário")
        if titulo in self.emprestimos:
            raise ErroLivroIndisponivel(titulo, "já emprestado")
        
        self.emprestimos[titulo] = usuario
        self.livros[titulo] = False
        print(f"{usuario} pegou '{titulo}' emprestado.")
    
    def devolver(self, usuario, titulo, dias_atraso=0):
        if titulo not in self.emprestimos or self.emprestimos[titulo] != usuario:
            raise ErroDevolucaoInvalida(usuario, titulo)
        
        del self.emprestimos[titulo]
        self.livros[titulo] = True
        
        if dias_atraso > 0:
            raise ErroEmprestimoAtrasado(usuario, titulo, dias_atraso)
        
        print(f"{usuario} devolveu '{titulo}'.")
    
    def reservar(self, usuario, titulo):
        if titulo in self.reservas:
            raise ErroLivroIndisponivel(titulo, "já possui uma reserva ativa")
        
        self.reservas[titulo] = usuario
        print(f"{usuario} reservou '{titulo}'.")

# Testes
biblioteca = Biblioteca()

# Tentativa de emprestar um livro já alugado
try:
    biblioteca.emprestar("Alice", "Python Essencial")
    biblioteca.emprestar("Bruno", "Python Essencial")
except ErroLivroIndisponivel as e:
    print(e)

# Tentativa de devolução inválida
try:
    biblioteca.devolver("Carlos", "Dominando Python")
except ErroDevolucaoInvalida as e:
    print(e)

# Tentativa de reserva de um livro já reservado
try:
    biblioteca.reservar("Daniela", "Python Essencial")
    biblioteca.reservar("Eduardo", "Python Essencial")
except ErroLivroIndisponivel as e:
    print(e)

# Erro ao passar um título inválido
try:
    biblioteca.emprestar("Fernanda", 12345)
except TypeError as e:
    print(e)

# Devolução atrasada
try:
    biblioteca.devolver("Alice", "Python Essencial", dias_atraso=4)
except ErroEmprestimoAtrasado as e:
    print(e)
