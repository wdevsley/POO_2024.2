## Exercício em Sala

Você foi contratado para desenvolver um sistema de gestão de biblioteca, onde os usuários podem emprestar, devolver e reservar livros. Seu objetivo é implementar exceções personalizadas para os seguintes problemas:

* Empréstimo de um livro indisponível (já emprestado ou reservado).
* Devolução de um livro que não foi emprestado pelo usuário.
* Tentativa de empréstimo com um valor inválido (ex: número ao invés de string para o título do livro).
* Atraso na devolução do livro, aplicando uma multa.

### Parte 1: Criando as Exceções Personalizadas

Crie as seguintes exceções, herdando de Exception:

1. LivroIndisponivelError:

* Deve receber dois parâmetros: titulo_livro e motivo.
* Exemplo de mensagem:
    * "O livro 'Python para Iniciantes' não pode ser emprestado: já está emprestado para outro usuário."
2. DevolucaoInvalidaError:
* Deve receber o nome do usuário e o livro que ele tentou devolver.
* Exemplo de mensagem:
    * "Usuário João tentou devolver 'Python Avançado', mas ele não pegou esse livro emprestado."
3. EmprestimoAtrasadoError:
* Deve receber o nome do usuário, o livro e a quantidade de dias de atraso.
* O sistema deve calcular a multa: multa = dias_atraso * 2.50 (2,50 reais por dia).
* Exemplo de mensagem:
    * "Usuário Maria atrasou a devolução de 'Machine Learning Básico' em 5 dias. Multa de 12.50 reais aplicada."
    
### Parte 2: Melhorando o Tratamento de Exceções

No código atual, se houver uma exceção diferente das listadas acima, ela será tratada de forma genérica. Adapte o código para capturar exceções específicas:
* ValueError: Quando um usuário tenta devolver um livro que **não pegou emprestado**.
* TypeError: Quando um usuário tenta **emprestar um livro passando um valor inválido**.
* EmprestimoAtrasadoError: Se um usuário atrasar a devolução, o sistema deve **exibir a multa**.


Dentro do except Exception, exiba uma mensagem genérica:
* "Erro inesperado! Por favor, entre em contato com a administração da biblioteca."

### Parte 3: Testando Exceções

Agora que o tratamento de exceções foi melhorado, escreva um código de teste que:

1. Crie uma biblioteca com alguns livros disponíveis.
2. Realize as seguintes operações, verificando o tratamento de erros:
* Tentar emprestar um livro que já está emprestado.
* Tentar devolver um livro que não foi emprestado.
* Tentar reservar um livro que já está reservado.
* Tentar emprestar um livro passando um número ao invés do título.
* Simular um usuário devolvendo um livro 5 dias após o prazo, aplicando a multa.

### Parte opcional

Adicionaa funcionalidades como:

* Histórico de empréstimos de cada usuário.
* Sistema de notificações para lembrar os usuários da devolução.
* Aumento da multa por reincidência de atrasos.
