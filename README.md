# Testes-unitarios-python-unittest
Esse repositório foi feito para uma atividade da disciplina de Engenharia de Software 1 e, tem o intuito de implementar um sistema simples em python, para em seguida testá-lo usando testes unitários

## Escolha da ferramenta
A ferramenta de testes unitários escolhida foi a PyUnit da biblioteca unittest

## Descrição da aplicação
A aplicação consiste em um sistema simples de uma biblioteca em Python, que simula as seguintes atividades:
- Biblioteca comprar novos livros para seu acervo;
- Aluno pegar livros emprestados;
- Aluno devolver livros emprestados;
- Biblioteca aplicar multas para alunos que devolveram o livro depois do prazo;
- Aluno pagar suas multas.

## Elaboração dos testes unitários
Ao todo foram implementados 18 testes unitários, que testam as seguintes funcionalidades:
- Construtores da Biblioteca, Aluno e Livro;
- Compra de livros que cabem no orçamento da Biblioteca e verificação do valor que foi descontado;
- Tentativa de compra de livros que não cabem no orçamento da Biblioteca;
- Emprestimo de livro do acervo da Biblioteca
- Tentativa de emprestimo de livro inexistente do acervo da Biblioteca;
- Devolução de um livro que o aluno fez o emprestimo;
- Tentativa de devolução de um livro que o aluno não fez o empréstimo;
- Aplicação de multa no aluno por atraso na devolução e verificação do valor cobrado pela multa;
- Pagamento das multas do aluno e verificação do valor removido do aluno e adicionado para a Biblioteca;
- Tentativa de pagamento de uma multa cujo valor é maior que o dinheiro do aluno;
- Tentativa de pegar um livro emprestado mas com o aluno possuindo multas pendentes.
